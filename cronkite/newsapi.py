import aiohttp
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Optional
from .core import NewsStory
from .config import SOURCE_WEIGHTS
from cronkite import get_logger

logger = get_logger(__name__)

class NewsAPIScraper:
    """Scrape news from NewsAPI.org"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
        
        # Categories to fetch from NewsAPI
        self.categories = [
            'general', 'world', 'politics', 'business', 
            'technology', 'science', 'health', 'entertainment'
        ]
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Get stories from NewsAPI across multiple categories"""
        stories = []
        
        # Convert cutoff_time to ISO format for NewsAPI
        from_date = cutoff_time.strftime('%Y-%m-%d')
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for category in self.categories:
                tasks.append(self._fetch_category(session, category, from_date))
            
            import asyncio
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                category = self.categories[i]
                if isinstance(result, Exception):
                    logger.error(f"Error fetching NewsAPI category {category}: {result}")
                elif isinstance(result, list):
                    logger.info(f"Collected {len(result)} stories from NewsAPI {category}")
                    stories.extend(result)
                else:
                    logger.warning(f"Unexpected result type from NewsAPI {category}: {type(result)}")
        
        logger.info(f"Total NewsAPI stories collected: {len(stories)}")
        return stories
    
    async def _fetch_category(self, session: aiohttp.ClientSession, 
                            category: str, from_date: str) -> List[NewsStory]:
        """Fetch stories for a specific category"""
        try:
            url = f"{self.base_url}/top-headlines"
            params = {
                'country': 'us',  # Can be expanded to multiple countries
                'category': category,
                'apiKey': self.api_key,
                'pageSize': 20,  # Max stories per category
                'language': 'en'
            }
            
            logger.info(f"Fetching NewsAPI category: {category}")
            
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if data.get('status') == 'ok':
                        articles = data.get('articles', [])
                        stories = []
                        
                        for article in articles:
                            story = self._parse_article(article, category)
                            if story:
                                stories.append(story)
                        
                        logger.info(f"Successfully parsed {len(stories)} stories from NewsAPI {category}")
                        return stories
                    else:
                        error_msg = data.get('message', 'Unknown error')
                        logger.error(f"NewsAPI error for {category}: {error_msg}")
                else:
                    logger.error(f"HTTP error {response.status} for NewsAPI {category}")
                    
        except Exception as e:
            logger.error(f"Error fetching NewsAPI category {category}: {e}")
        
        return []
    
    def _parse_article(self, article: Dict, category: str) -> Optional[NewsStory]:
        """Parse a NewsAPI article into NewsStory format"""
        try:
            # Extract article data
            title = article.get('title', '')
            description = article.get('description', '')
            url = article.get('url', '')
            source_name = article.get('source', {}).get('name', 'Unknown')
            published_at = article.get('publishedAt', '')
            
            # Skip articles without essential data
            if not title or not url:
                return None
            
            # Parse publication date
            try:
                if published_at:
                    # NewsAPI uses ISO 8601 format
                    published = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                else:
                    published = datetime.now(timezone.utc)
            except Exception:
                published = datetime.now(timezone.utc)
            
            # Create source name with NewsAPI prefix
            full_source_name = f"NewsAPI {source_name}"
            
            # Get source weight (default to 0.5 if not found)
            source_weight = SOURCE_WEIGHTS.get(full_source_name, 0.5)
            
            # Create NewsStory
            story = NewsStory(
                title=title,
                summary=description or '',
                url=url,
                source=full_source_name,
                published=published,
                category=self._map_category(category),
                source_weights=[source_weight]
            )
            
            return story
            
        except Exception as e:
            logger.error(f"Error parsing NewsAPI article: {e}")
            return None
    
    def _map_category(self, newsapi_category: str) -> str:
        """Map NewsAPI categories to our internal categories"""
        category_mapping = {
            'general': 'International relations',
            'world': 'International relations',
            'politics': 'Politics and elections',
            'business': 'Business and economy',
            'technology': 'Business and economy',
            'science': 'Business and economy',
            'health': 'International relations',
            'entertainment': 'International relations'
        }
        return category_mapping.get(newsapi_category, 'International relations') 