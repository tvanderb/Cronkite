from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re
import logging
import difflib
from cronkite.config import SOURCE_WEIGHTS, OPINION_KEYWORDS, OPINION_URL_PATTERNS, OPINION_REDDIT_FLAIRS

@dataclass
class NewsStory:
    """Standardized news story format"""
    title: str
    summary: str
    url: str
    source: str
    published: datetime
    category: Optional[str] = None
    location: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)  # All sources reporting this story
    source_weights: List[float] = field(default_factory=list)  # Weights for each source
    dedup_key: Optional[str] = None  # For deduplication
    reddit_flair: Optional[str] = None  # Reddit post flair for filtering
    
    def __post_init__(self):
        if not self.sources and self.source:
            self.sources.append(self.source)

class NewsAggregator:
    """Main aggregator that coordinates all data sources"""
    
    def __init__(self):
        from .rss import RSSFeedScraper
        from .web import WebScraper
        from .social import SocialMediaScraper
        self.stories: List[NewsStory] = []
        self.scrapers = {
            'rss': RSSFeedScraper(),
            'web': WebScraper(),
            'social': SocialMediaScraper()
        }
        
    async def collect_all_stories(self, hours_back: int = 24, limit: int = 100) -> List[NewsStory]:
        """Collect stories from all sources"""
        from datetime import timezone
        cutoff_time = datetime.now(timezone.utc) - timedelta(hours=hours_back)
        all_stories = []
        
        # Run all scrapers concurrently
        import asyncio
        tasks = []
        for scraper_name, scraper in self.scrapers.items():
            tasks.append(scraper.get_stories(cutoff_time))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            scraper_name = list(self.scrapers.keys())[i]
            if isinstance(result, Exception):
                logging.error(f"Error in {scraper_name} scraper: {result}")
            elif isinstance(result, list):
                all_stories.extend(result)
        
        # Deduplicate and sort
        deduped = self._deduplicate_stories(all_stories, limit=limit)
        # Sort by total source weight, then by recency
        deduped.sort(key=lambda s: (sum(s.source_weights), s.published), reverse=True)
        self.stories = deduped
        return self.stories
    
    def _normalize_title(self, title: str) -> str:
        return re.sub(r'[^\w\s]', '', title.lower()).strip()

    def _is_opinion_piece(self, story: NewsStory) -> bool:
        """Check if a story is likely an opinion piece based on keywords, URL patterns, and Reddit flairs"""
        # Check title and summary for opinion keywords
        text_to_check = f"{story.title} {story.summary}".lower()
        if any(keyword.lower() in text_to_check for keyword in OPINION_KEYWORDS):
            return True
        
        # Check URL for opinion patterns
        if story.url:
            url_lower = story.url.lower()
            if any(pattern.lower() in url_lower for pattern in OPINION_URL_PATTERNS):
                return True
        
        # Check Reddit flair (if source is Reddit)
        if story.source.startswith('Reddit') and hasattr(story, 'reddit_flair'):
            if story.reddit_flair and any(flair.lower() in story.reddit_flair.lower() for flair in OPINION_REDDIT_FLAIRS):
                return True
        
        return False

    def _deduplicate_stories(self, stories: List[NewsStory], limit: int = 100) -> List[NewsStory]:
        """Remove duplicate stories using fuzzy title matching and merge sources/weights. Output is round-robin by category."""
        SIMILARITY_THRESHOLD = 0.85  # Configurable
        unique_stories = []
        for story in sorted(stories, key=lambda x: x.published, reverse=True):
            # Filter out opinion pieces
            if self._is_opinion_piece(story):
                continue
            norm_title = self._normalize_title(story.title)
            found_duplicate = False
            for unique in unique_stories:
                unique_norm_title = self._normalize_title(unique.title)
                similarity = difflib.SequenceMatcher(None, norm_title, unique_norm_title).ratio()
                if similarity >= SIMILARITY_THRESHOLD:
                    # Merge sources and weights
                    for src, wgt in zip(story.sources, story.source_weights):
                        if src not in unique.sources:
                            unique.sources.append(src)
                            unique.source_weights.append(wgt)
                    # Optionally, keep the story with the highest total weight
                    if sum(story.source_weights) > sum(unique.source_weights):
                        unique.title = story.title
                        unique.summary = story.summary
                        unique.url = story.url
                        unique.published = story.published
                        unique.category = story.category
                        unique.location = story.location
                        unique.tags = story.tags
                    found_duplicate = True
                    break
            if not found_duplicate:
                unique_stories.append(story)
        # Sort by total source weight, then by recency
        unique_stories.sort(key=lambda s: (sum(s.source_weights), s.published), reverse=True)
        # Round-robin by category
        from collections import defaultdict, deque
        cat_map = defaultdict(deque)
        for story in unique_stories:
            cat = story.category or 'Uncategorized'
            cat_map[cat].append(story)
        output = []
        while len(output) < limit and any(cat_map.values()):
            for cat in list(cat_map.keys()):
                if cat_map[cat]:
                    output.append(cat_map[cat].popleft())
                    if len(output) >= limit:
                        break
        return output
    
    def prepare_for_ingestion(self) -> Dict:
        """Format stories for Claude API consumption"""
        return {
            'timestamp': datetime.now().isoformat(),
            'story_count': len(self.stories),
            'stories': [asdict(story) for story in self.stories],
            'categories': self._get_category_summary()
        }
    
    def _get_category_summary(self) -> Dict[str, int]:
        """Get count of stories by category"""
        categories = {}
        for story in self.stories:
            cat = story.category or 'Uncategorized'
            categories[cat] = categories.get(cat, 0) + 1
        return categories 