from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re
import logging
import difflib
from cronkite.config import SOURCE_WEIGHTS, OPINION_KEYWORDS, OPINION_URL_PATTERNS, OPINION_REDDIT_FLAIRS, HIGH_RELIABILITY_SOURCES, SOURCE_HIERARCHY
from urllib.parse import urlparse, parse_qs, urlunparse

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
    
    def _canonicalize_url(self, url: str) -> str:
        """Canonicalize URL by removing tracking parameters and normalizing"""
        if not url:
            return url
        try:
            parsed = urlparse(url)
            # Remove common tracking parameters
            query_params = parse_qs(parsed.query)
            filtered_params = {k: v for k, v in query_params.items() 
                             if not any(tracker in k.lower() for tracker in 
                                      ['utm_', 'ref_', 'source', 'campaign', 'medium'])}
            # Rebuild URL without tracking params
            clean_query = '&'.join([f"{k}={v[0]}" for k, v in filtered_params.items()])
            return urlunparse((parsed.scheme, parsed.netloc, parsed.path, 
                             parsed.params, clean_query, parsed.fragment))
        except Exception:
            return url

    def _normalize_title(self, title: str) -> str:
        """Enhanced title normalization"""
        if not title:
            return ""
        # Remove common prefixes/suffixes
        prefixes_to_remove = [
            'breaking:', 'breaking news:', 'update:', 'just in:', 'live:',
            'exclusive:', 'analysis:', 'opinion:', 'comment:', 'editorial:'
        ]
        title_lower = title.lower()
        for prefix in prefixes_to_remove:
            if title_lower.startswith(prefix):
                title = title[len(prefix):].strip()
                break
        
        # Normalize punctuation and whitespace
        import re
        title = re.sub(r'[^\w\s]', ' ', title)  # Replace punctuation with spaces
        title = re.sub(r'\s+', ' ', title)      # Normalize whitespace
        return title.lower().strip()

    def _calculate_similarity_score(self, story1: NewsStory, story2: NewsStory) -> float:
        """Calculate weighted similarity score between two stories with source-aware adjustments"""
        # Normalize titles
        title1 = self._normalize_title(story1.title)
        title2 = self._normalize_title(story2.title)
        
        # Calculate similarities
        title_similarity = difflib.SequenceMatcher(None, title1, title2).ratio()
        
        # URL similarity (if both have URLs)
        url_similarity = 0.0
        if story1.url and story2.url:
            url1 = self._canonicalize_url(story1.url)
            url2 = self._canonicalize_url(story2.url)
            if url1 == url2:
                url_similarity = 1.0
            else:
                url_similarity = difflib.SequenceMatcher(None, url1, url2).ratio()
        
        # Summary similarity
        summary_similarity = 0.0
        if story1.summary and story2.summary:
            summary_similarity = difflib.SequenceMatcher(None, 
                story1.summary.lower(), story2.summary.lower()).ratio()
        
        # Base weighted score: title (60%), URL (30%), summary (10%)
        base_score = (title_similarity * 0.6 + 
                     url_similarity * 0.3 + 
                     summary_similarity * 0.1)
        
        # Source-aware adjustments
        source_boost = self._calculate_source_boost(story1, story2)
        
        return min(1.0, base_score + source_boost)

    def _calculate_source_boost(self, story1: NewsStory, story2: NewsStory) -> float:
        """Calculate source-aware boost for similarity scoring"""
        boost = 0.0
        
        # Cross-source verification bonus
        sources1 = set(story1.sources)
        sources2 = set(story2.sources)
        
        # If both stories have high-reliability sources, boost confidence
        high_rel1 = any(src in HIGH_RELIABILITY_SOURCES for src in sources1)
        high_rel2 = any(src in HIGH_RELIABILITY_SOURCES for src in sources2)
        
        if high_rel1 and high_rel2:
            boost += 0.1  # 10% boost for cross-verification by reliable sources
        
        # If stories share any sources, boost significantly
        if sources1 & sources2:
            boost += 0.2  # 20% boost for same source
        
        # Original vs syndicated detection
        if self._is_likely_syndicated(story1, story2):
            boost += 0.15  # 15% boost for syndicated content
        
        return boost

    def _is_likely_syndicated(self, story1: NewsStory, story2: NewsStory) -> bool:
        """Detect if one story is likely syndicated from the other"""
        # Check if URLs are very similar but from different domains
        if story1.url and story2.url:
            url1 = self._canonicalize_url(story1.url)
            url2 = self._canonicalize_url(story2.url)
            
            try:
                domain1 = urlparse(url1).netloc
                domain2 = urlparse(url2).netloc
                
                # If different domains but very similar content, likely syndicated
                if domain1 != domain2:
                    title_sim = difflib.SequenceMatcher(None, 
                        self._normalize_title(story1.title), 
                        self._normalize_title(story2.title)).ratio()
                    return title_sim > 0.8
            except:
                pass
        
        return False

    def _get_preferred_story(self, story1: NewsStory, story2: NewsStory) -> NewsStory:
        """Determine which story to keep based on source hierarchy and other factors"""
        # Calculate source hierarchy scores
        score1 = sum(SOURCE_HIERARCHY.get(src, 0) for src in story1.sources)
        score2 = sum(SOURCE_HIERARCHY.get(src, 0) for src in story2.sources)
        
        # If hierarchy scores are close, consider other factors
        if abs(score1 - score2) <= 2:
            # Prefer story with more sources (more verification)
            if len(story1.sources) != len(story2.sources):
                return story1 if len(story1.sources) > len(story2.sources) else story2
            
            # Prefer more recent story
            if story1.published != story2.published:
                return story1 if story1.published > story2.published else story2
            
            # Prefer story with higher total source weight
            weight1 = sum(story1.source_weights)
            weight2 = sum(story2.source_weights)
            return story1 if weight1 > weight2 else story2
        
        # Use hierarchy score as primary factor
        return story1 if score1 > score2 else story2

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
        """Enhanced deduplication with source-aware logic"""
        SIMILARITY_THRESHOLD = 0.75  # Lowered due to better scoring
        TEMPORAL_WINDOW_HOURS = 12   # Only compare stories within 12 hours
        
        unique_stories = []
        for story in sorted(stories, key=lambda x: x.published, reverse=True):
            # Filter out opinion pieces
            if self._is_opinion_piece(story):
                continue
            
            # Canonicalize URL
            story.url = self._canonicalize_url(story.url)
            
            found_duplicate = False
            for unique in unique_stories:
                # Check temporal window
                time_diff = abs((story.published - unique.published).total_seconds() / 3600)
                if time_diff > TEMPORAL_WINDOW_HOURS:
                    continue
                
                # Calculate weighted similarity with source-aware adjustments
                similarity = self._calculate_similarity_score(story, unique)
                if similarity >= SIMILARITY_THRESHOLD:
                    # Merge sources and weights
                    for src, wgt in zip(story.sources, story.source_weights):
                        if src not in unique.sources:
                            unique.sources.append(src)
                            unique.source_weights.append(wgt)
                    
                    # Use source-aware story selection
                    preferred_story = self._get_preferred_story(story, unique)
                    if preferred_story == story:
                        unique.title = story.title
                        unique.summary = story.summary
                        unique.url = story.url
                        unique.published = story.published
                        unique.category = story.category
                        unique.location = story.location
                        unique.tags = story.tags
                        unique.reddit_flair = story.reddit_flair
                    
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