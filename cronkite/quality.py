import logging
from urllib.parse import urlparse
from typing import List, Dict, Optional, Tuple
from .core import NewsStory
from .config import (
    UNRELIABLE_SOURCES, DOMAIN_REPUTATION, CONTENT_QUALITY_THRESHOLDS,
    GEOGRAPHIC_DIVERSITY, SOURCE_WEIGHTS, OPINION_KEYWORDS
)
import re
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class QualityFilter:
    """Filter and improve source quality"""
    
    def __init__(self):
        self.geographic_keywords = {
            'north_america': ['united states', 'canada', 'mexico', 'us', 'usa', 'american'],
            'europe': ['europe', 'european', 'uk', 'britain', 'france', 'germany', 'italy', 'spain'],
            'asia': ['asia', 'asian', 'china', 'japan', 'india', 'korea', 'singapore', 'hong kong'],
            'other': ['africa', 'african', 'australia', 'australian', 'middle east', 'latin america']
        }
        self.opinion_keywords = set(OPINION_KEYWORDS)
    
    def filter_stories(self, stories: List[NewsStory]) -> List[NewsStory]:
        """Apply all quality filters to stories"""
        logging.info(f"Applying quality filters to {len(stories)} stories")
        
        filtered_stories = []
        for story in stories:
            if self._is_quality_story(story):
                # Apply source quality adjustments
                self._adjust_source_quality(story)
                filtered_stories.append(story)
            else:
                logging.debug(f"Filtered out low-quality story: {story.title[:50]}...")
        
        logging.info(f"Quality filtering complete: {len(filtered_stories)} stories passed")
        return filtered_stories
    
    def _is_quality_story(self, story: NewsStory) -> bool:
        """Check if a story meets quality standards"""
        # Check for unreliable sources
        if self._is_unreliable_source(story):
            return False
        
        # Check content quality
        if not self._meets_content_standards(story):
            return False
        
        # Check domain reputation
        if self._get_domain_reputation(story.url) < 0.3:
            return False
        
        # Check for opinion keywords in title
        title_lower = story.title.lower()
        if any(keyword in title_lower for keyword in self.opinion_keywords):
            return False
        
        return True
    
    def _is_unreliable_source(self, story: NewsStory) -> bool:
        """Check if story comes from unreliable source"""
        if not story.url:
            return False
        
        try:
            domain = urlparse(story.url).netloc.lower()
            return domain in UNRELIABLE_SOURCES
        except Exception:
            return False
    
    def _meets_content_standards(self, story: NewsStory) -> bool:
        """Check if story meets content quality standards"""
        thresholds = CONTENT_QUALITY_THRESHOLDS
        
        # Check title length
        if len(story.title) < thresholds['min_title_length']:
            return False
        if len(story.title) > thresholds['max_title_length']:
            return False
        
        # Check summary length
        if len(story.summary) < thresholds['min_summary_length']:
            return False
        if len(story.summary) > thresholds['max_summary_length']:
            return False
        
        # Check word count (rough estimate)
        total_text = f"{story.title} {story.summary}"
        word_count = len(total_text.split())
        if word_count < thresholds['min_word_count']:
            return False
        if word_count > thresholds['max_word_count']:
            return False
        
        return True
    
    def _get_domain_reputation(self, url: str) -> float:
        """Get domain reputation score"""
        if not url:
            return 0.5  # Default score for unknown domains
        
        try:
            domain = urlparse(url).netloc.lower()
            return DOMAIN_REPUTATION.get(domain, 0.5)
        except Exception:
            return 0.5
    
    def _adjust_source_quality(self, story: NewsStory):
        """Adjust source weights based on domain reputation"""
        domain_score = self._get_domain_reputation(story.url)
        
        # Adjust source weights based on domain reputation
        if story.source_weights:
            # Boost weight if domain has high reputation
            if domain_score > 0.8:
                story.source_weights[0] = min(1.0, story.source_weights[0] * 1.1)
            # Reduce weight if domain has low reputation
            elif domain_score < 0.4:
                story.source_weights[0] = max(0.1, story.source_weights[0] * 0.8)
    
    def analyze_geographic_diversity(self, stories: List[NewsStory]) -> Dict[str, int]:
        """Analyze geographic distribution of stories"""
        geographic_counts = {
            'north_america': 0,
            'europe': 0,
            'asia': 0,
            'other': 0
        }
        
        for story in stories:
            region = self._classify_geographic_region(story)
            geographic_counts[region] += 1
        
        total = len(stories)
        if total > 0:
            logging.info(f"Geographic distribution: NA: {geographic_counts['north_america']}/{total} "
                        f"({geographic_counts['north_america']/total:.1%}), "
                        f"EU: {geographic_counts['europe']}/{total} ({geographic_counts['europe']/total:.1%}), "
                        f"AS: {geographic_counts['asia']}/{total} ({geographic_counts['asia']/total:.1%}), "
                        f"Other: {geographic_counts['other']}/{total} ({geographic_counts['other']/total:.1%})")
        
        return geographic_counts
    
    def _classify_geographic_region(self, story: NewsStory) -> str:
        """Classify story by geographic region based on content"""
        text_to_check = f"{story.title} {story.summary}".lower()
        
        for region, keywords in self.geographic_keywords.items():
            if any(keyword in text_to_check for keyword in keywords):
                return region
        
        return 'other'
    
    def get_quality_metrics(self, stories: List[NewsStory]) -> Dict[str, float]:
        """Calculate quality metrics for the story collection"""
        if not stories:
            return {}
        
        total_stories = len(stories)
        high_reputation_count = 0
        total_domain_score = 0
        
        for story in stories:
            domain_score = self._get_domain_reputation(story.url)
            total_domain_score += domain_score
            if domain_score > 0.8:
                high_reputation_count += 1
        
        return {
            'avg_domain_reputation': total_domain_score / total_stories,
            'high_reputation_ratio': high_reputation_count / total_stories,
            'total_stories': total_stories
        }

class StoryScorer:
    """
    Advanced story scoring system that identifies the most interesting, unique, 
    and impactful stories, including underreported important stories.
    """
    
    def __init__(self):
        self.impact_keywords = {
            'high_impact': {
                'global', 'worldwide', 'international', 'crisis', 'emergency', 'outbreak',
                'pandemic', 'war', 'conflict', 'election', 'presidential', 'breakthrough',
                'discovery', 'revolutionary', 'historic', 'unprecedented', 'first_time',
                'major', 'significant', 'critical', 'urgent', 'deadline', 'deadline',
                'billion', 'trillion', 'millions', 'thousands', 'casualties', 'deaths',
                'arrest', 'indictment', 'conviction', 'verdict', 'supreme_court',
                'congress', 'senate', 'house', 'legislation', 'bill', 'law', 'policy',
                'regulation', 'ban', 'restriction', 'approval', 'rejection', 'veto'
            },
            'medium_impact': {
                'announcement', 'launch', 'release', 'update', 'change', 'new',
                'study', 'research', 'finding', 'report', 'analysis', 'survey',
                'poll', 'election', 'vote', 'decision', 'ruling', 'settlement',
                'agreement', 'deal', 'partnership', 'merger', 'acquisition',
                'investment', 'funding', 'grant', 'award', 'recognition'
            }
        }
        
        self.scarcity_indicators = {
            'exclusive', 'first', 'breaking', 'developing', 'emerging', 'newly_discovered',
            'previously_unknown', 'hidden', 'revealed', 'exposed', 'leaked', 'whistleblower',
            'investigation', 'probe', 'inquiry', 'audit', 'review', 'analysis',
            'study_finds', 'research_shows', 'data_reveals', 'report_indicates'
        }
        
        self.urgency_indicators = {
            'breaking', 'urgent', 'immediate', 'deadline', 'today', 'tonight',
            'this_week', 'this_month', 'deadline', 'expires', 'expiration',
            'last_chance', 'final', 'conclusion', 'deadline', 'countdown'
        }
        
        # Keywords that suggest important but underreported stories
        self.underreported_indicators = {
            'whistleblower', 'leak', 'exposed', 'revealed', 'investigation',
            'probe', 'inquiry', 'audit', 'review', 'analysis', 'study_finds',
            'research_shows', 'data_reveals', 'report_indicates', 'previously_unknown',
            'hidden', 'secret', 'confidential', 'classified', 'internal',
            'behind_the_scenes', 'exclusive', 'first_to_report', 'breaking_news'
        }
    
    def score_stories(self, stories: List['NewsStory'], hours_back: int = 24) -> List[Tuple[float, 'NewsStory']]:
        """
        Score stories based on multiple factors including impact, scarcity, 
        source quality, and underreported importance.
        """
        scored_stories = []
        from datetime import timezone
        cutoff_time = datetime.now(timezone.utc) - timedelta(hours=hours_back)
        
        # Calculate baseline metrics
        source_coverage = self._calculate_source_coverage(stories)
        topic_coverage = self._calculate_topic_coverage(stories)
        
        for story in stories:
            if story.published < cutoff_time:
                continue
                
            score = self._calculate_story_score(
                story, source_coverage, topic_coverage, hours_back
            )
            scored_stories.append((score, story))
        
        # Sort by score (highest first)
        scored_stories.sort(key=lambda x: x[0], reverse=True)
        
        logger.info(f"Scored {len(scored_stories)} stories")
        return scored_stories
    
    def _calculate_story_score(self, story, source_coverage: Dict, topic_coverage: Dict, hours_back: int) -> float:
        """Calculate comprehensive story score"""
        score = 0.0
        
        # Base source quality score (0-1)
        source_score = self._get_source_score(story)
        score += source_score * 0.3
        
        # Impact score based on keywords and content analysis
        impact_score = self._calculate_impact_score(story)
        score += impact_score * 0.25
        
        # Scarcity score - how unique/rare this story is
        scarcity_score = self._calculate_scarcity_score(story, source_coverage, topic_coverage)
        score += scarcity_score * 0.2
        
        # Underreported importance score
        underreported_score = self._calculate_underreported_score(story, source_coverage)
        score += underreported_score * 0.15
        
        # Recency score (newer stories get higher scores)
        recency_score = self._calculate_recency_score(story, hours_back)
        score += recency_score * 0.1
        
        return score
    
    def _get_source_score(self, story) -> float:
        """Get source reputation score"""
        domain = urlparse(story.url).netloc
        return DOMAIN_REPUTATION.get(domain, 0.5)
    
    def _calculate_impact_score(self, story) -> float:
        """Calculate impact score based on keywords and content"""
        title_lower = story.title.lower()
        content_lower = getattr(story, 'summary', '').lower()
        text = f"{title_lower} {content_lower}"
        
        score = 0.0
        
        # High impact keywords
        high_impact_count = sum(1 for keyword in self.impact_keywords['high_impact'] 
                               if keyword.replace('_', ' ') in text)
        score += high_impact_count * 0.1
        
        # Medium impact keywords
        medium_impact_count = sum(1 for keyword in self.impact_keywords['medium_impact'] 
                                 if keyword.replace('_', ' ') in text)
        score += medium_impact_count * 0.05
        
        # Cap the impact score
        return min(score, 1.0)
    
    def _calculate_scarcity_score(self, story, source_coverage: Dict, topic_coverage: Dict) -> float:
        """Calculate how unique/scarce this story is"""
        score = 0.0
        
        # Check if this source is covering this story
        source = story.source
        if source in source_coverage:
            # Lower score if many sources are covering similar stories
            coverage_count = source_coverage[source]
            if coverage_count > 10:
                score -= 0.2
            elif coverage_count > 5:
                score -= 0.1
        
        # Check for scarcity indicators in title
        title_lower = story.title.lower()
        scarcity_count = sum(1 for indicator in self.scarcity_indicators 
                            if indicator.replace('_', ' ') in title_lower)
        score += scarcity_count * 0.1
        
        # Bonus for exclusive or first-to-report indicators
        if any(indicator in title_lower for indicator in ['exclusive', 'first', 'breaking']):
            score += 0.2
        
        return max(score, 0.0)
    
    def _calculate_underreported_score(self, story, source_coverage: Dict) -> float:
        """Calculate score for potentially underreported important stories"""
        score = 0.0
        
        title_lower = story.title.lower()
        content_lower = getattr(story, 'summary', '').lower()
        text = f"{title_lower} {content_lower}"
        
        # Check for underreported indicators
        underreported_count = sum(1 for indicator in self.underreported_indicators 
                                 if indicator.replace('_', ' ') in text)
        score += underreported_count * 0.1
        
        # Bonus for high-impact stories from fewer sources
        if self._calculate_impact_score(story) > 0.3:
            source = story.source
            if source in source_coverage and source_coverage[source] < 3:
                score += 0.3  # Important story with limited coverage
        
        # Bonus for whistleblower/leak stories
        if any(keyword in text for keyword in ['whistleblower', 'leak', 'exposed', 'revealed']):
            score += 0.2
        
        return min(score, 1.0)
    
    def _calculate_recency_score(self, story, hours_back: int) -> float:
        """Calculate recency score"""
        from datetime import timezone
        now = datetime.now(timezone.utc)
        age_hours = (now - story.published).total_seconds() / 3600
        
        if age_hours <= 1:
            return 1.0
        elif age_hours <= 6:
            return 0.8
        elif age_hours <= 12:
            return 0.6
        elif age_hours <= 24:
            return 0.4
        else:
            return 0.2
    
    def _calculate_source_coverage(self, stories: List) -> Dict[str, int]:
        """Calculate how many stories each source is covering"""
        source_counts = {}
        for story in stories:
            source_counts[story.source] = source_counts.get(story.source, 0) + 1
        return source_counts
    
    def _calculate_topic_coverage(self, stories: List) -> Dict[str, int]:
        """Calculate topic coverage (simplified keyword-based)"""
        topic_counts = {}
        for story in stories:
            # Extract key topics from title
            title_words = story.title.lower().split()
            for word in title_words:
                if len(word) > 4:  # Skip short words
                    topic_counts[word] = topic_counts.get(word, 0) + 1
        return topic_counts
    
    def select_top_stories(self, scored_stories: List[Tuple[float, 'NewsStory']], 
                          max_stories: int = 50, diversity_threshold: float = 0.1) -> List['NewsStory']:
        """
        Select top stories with diversity considerations to avoid topic clustering
        """
        selected = []
        selected_topics = set()
        
        for score, story in scored_stories[:max_stories * 2]:  # Consider more candidates
            if len(selected) >= max_stories:
                break
            
            # Extract main topic from title
            main_topic = self._extract_main_topic(story.title)
            
            # Check if we need more diversity
            if main_topic in selected_topics and len(selected) > max_stories // 2:
                # Only add if score is significantly higher
                if score > diversity_threshold:
                    selected.append(story)
                    selected_topics.add(main_topic)
            else:
                selected.append(story)
                selected_topics.add(main_topic)
        
        logger.info(f"Selected {len(selected)} diverse top stories from {len(scored_stories)} scored stories")
        return selected
    
    def _extract_main_topic(self, title: str) -> str:
        """Extract main topic from title for diversity checking"""
        # Simple approach: use the first significant noun phrase
        words = title.lower().split()
        for word in words:
            if len(word) > 4 and not word in ['about', 'with', 'from', 'this', 'that', 'they', 'their']:
                return word
        return 'general' 