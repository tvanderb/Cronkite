import aiohttp
import feedparser
import logging
from datetime import datetime
from typing import List, Optional
from bs4 import BeautifulSoup
from .core import NewsStory
import asyncio
from cronkite.config import SOURCE_WEIGHTS

class RSSFeedScraper:
    """RSS feed scraper for major news sources"""
    
    RSS_FEEDS = [
        ('BBC World', 'https://feeds.bbci.co.uk/news/world/rss.xml'),
        ('Guardian World', 'https://www.theguardian.com/world/rss'),
        ('Reuters World', 'https://feeds.reuters.com/reuters/worldnews'),  # Keep but expect some failures
        ('CNN World', 'http://rss.cnn.com/rss/edition.rss'),
        ('ABC News', 'https://abcnews.go.com/abcnews/internationalheadlines'),
        ('NPR World', 'https://feeds.npr.org/1004/rss.xml'),  # Fixed URL
        ('Al Jazeera', 'https://www.aljazeera.com/xml/rss/all.xml'),
        # International sources
        ('Le Monde', 'https://www.lemonde.fr/rss/une.xml'),
        ('Der Spiegel', 'https://www.spiegel.de/international/index.rss'),
        ('El País', 'https://elpais.com/rss/elpais_inenglish.xml'),
        ('La Repubblica', 'https://www.repubblica.it/rss/homepage/rss2.0.xml'),
        ('Asahi Shimbun', 'https://www.asahi.com/ajw/rss/ajw.rdf'),
        ('South China Morning Post', 'https://www.scmp.com/rss/91/feed'),
        # Specialized sources
        ('The Economist', 'https://www.economist.com/international/rss.xml'),
        ('Financial Times', 'https://www.ft.com/world?format=rss'),
        ('Nature', 'https://www.nature.com/nature.rss'),
        ('Science', 'https://www.science.org/rss/news_current.xml'),
        ('The Atlantic', 'https://www.theatlantic.com/feed/all/'),
        ('New Yorker', 'https://www.newyorker.com/feed/everything'),
        # Regional/Alternative sources
        ('Associated Press', 'https://feeds.ap.org/ap/APTopNews'),
        ('Agence France-Presse', 'https://www.afp.com/en/news-hub/rss'),
        ('Bloomberg', 'https://feeds.bloomberg.com/politics/news.rss'),
        ('Vice News', 'https://www.vice.com/en/rss'),
        ('Vox', 'https://www.vox.com/rss/index.xml'),
        ('Politico', 'https://www.politico.com/rss/politicopicks.xml'),
    ]
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Fetch stories from RSS feeds"""
        stories = []
        
        connector = aiohttp.TCPConnector(ssl=False, limit=10)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for source_name, feed_url in self.RSS_FEEDS:
                tasks.append(self._fetch_rss_feed(session, source_name, feed_url, cutoff_time))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for result in results:
                if isinstance(result, list):
                    stories.extend(result)
        
        return stories
    
    async def _fetch_rss_feed(self, session: aiohttp.ClientSession, 
                            source_name: str, feed_url: str, 
                            cutoff_time: datetime) -> List[NewsStory]:
        """Fetch and parse individual RSS feed with comprehensive logging"""
        try:
            logging.info(f"Fetching RSS feed: {source_name} from {feed_url}")
            
            timeout = aiohttp.ClientTimeout(total=30, connect=10)
            
            async with session.get(feed_url, timeout=timeout, 
                                headers={'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'}) as response:
                logging.info(f"Response status for {source_name}: {response.status}")
                if response.status == 200:
                    content = await response.text()
                    stories = self._parse_rss_content(content, source_name, cutoff_time)
                    logging.info(f"Successfully parsed {len(stories)} stories from {source_name}")
                    if len(stories) == 0:
                        logging.warning(f"No recent stories found for {source_name} (cutoff: {cutoff_time})")
                    return stories
                else:
                    logging.error(f"HTTP error {response.status} for {source_name} from {feed_url}")
        except asyncio.TimeoutError:
            logging.error(f"Timeout error for {source_name} from {feed_url}")
        except aiohttp.ClientError as e:
            logging.error(f"Client error for {source_name} from {feed_url}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error for {source_name} from {feed_url}: {e}")
        return []
    
    def _parse_rss_content(self, content: str, source_name: str, 
                          cutoff_time: datetime) -> List[NewsStory]:
        """Parse RSS XML content"""
        stories = []
        try:
            feed = feedparser.parse(content)
            for entry in feed.entries:
                pub_date = self._parse_date(str(entry.get('published', '') or ''))
                if pub_date and pub_date > cutoff_time:
                    story = NewsStory(
                        title=str(entry.get('title', '') or ''),
                        summary=self._clean_html(str(entry.get('summary', entry.get('description', '')) or '')),
                        url=str(entry.get('link', '') or ''),
                        source=source_name,
                        published=pub_date,
                        category=self._categorize_story(str(entry.get('title', '') or '') + ' ' + str(entry.get('summary', '') or '')),
                        source_weights=[SOURCE_WEIGHTS.get(source_name, 0.5)]
                    )
                    stories.append(story)
        except Exception as e:
            logging.error(f"Error parsing RSS for {source_name}: {e}")
        return stories
    
    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """Parse various date formats and ensure timezone awareness"""
        if not date_str:
            return None
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(date_str)
            # Ensure both dates are timezone-aware or naive
            if dt.tzinfo is None:
                # Make it timezone-aware (assume UTC if no timezone)
                from datetime import timezone
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except:
            return None
    
    def _clean_html(self, text: str) -> str:
        """Remove HTML tags and clean text"""
        if not text:
            return ""
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text().strip()[:300]  # Limit summary length
    
    def _categorize_story(self, text: str) -> str:
        """Simple keyword-based categorization"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['war', 'attack', 'military', 'conflict', 'strike', 'bomb']):
            return 'Armed conflicts and attacks'
        elif any(word in text_lower for word in ['flood', 'earthquake', 'disaster', 'accident', 'crash']):
            return 'Disasters and accidents'
        elif any(word in text_lower for word in ['election', 'politics', 'government', 'parliament', 'president']):
            return 'Politics and elections'
        elif any(word in text_lower for word in ['crime', 'court', 'arrest', 'trial', 'lawsuit']):
            return 'Law and crime'
        elif any(word in text_lower for word in ['economy', 'market', 'trade', 'business', 'financial']):
            return 'Business and economy'
        else:
            return 'International relations' 