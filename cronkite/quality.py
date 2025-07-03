import logging
from urllib.parse import urlparse
from typing import List, Dict, Optional, Tuple
from .core import NewsStory
from .config import (
    UNRELIABLE_SOURCES, DOMAIN_REPUTATION, CONTENT_QUALITY_THRESHOLDS,
    GEOGRAPHIC_DIVERSITY, SOURCE_WEIGHTS
)

class QualityFilter:
    """Filter and improve source quality"""
    
    def __init__(self):
        self.geographic_keywords = {
            'north_america': ['united states', 'canada', 'mexico', 'us', 'usa', 'american'],
            'europe': ['europe', 'european', 'uk', 'britain', 'france', 'germany', 'italy', 'spain'],
            'asia': ['asia', 'asian', 'china', 'japan', 'india', 'korea', 'singapore', 'hong kong'],
            'other': ['africa', 'african', 'australia', 'australian', 'middle east', 'latin america']
        }
    
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