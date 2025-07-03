import aiohttp
from datetime import datetime, timezone
from typing import List
from .core import NewsStory
from .config import GOVERNMENT_RSS_FEEDS, ACADEMIC_RSS_FEEDS, INDUSTRY_RSS_FEEDS, SOURCE_WEIGHTS
from cronkite import get_logger

logger = get_logger(__name__)

class GovernmentScraper:
    """Scrape government RSS feeds"""
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Get stories from government sources"""
        stories = []
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for source_name, feed_url in GOVERNMENT_RSS_FEEDS:
                tasks.append(self._fetch_government_feed(session, source_name, feed_url, cutoff_time))
            
            import asyncio
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                source_name = GOVERNMENT_RSS_FEEDS[i][0]
                if isinstance(result, Exception):
                    logger.error(f"Error fetching government source {source_name}: {result}")
                elif isinstance(result, list):
                    logger.info(f"Collected {len(result)} stories from government source {source_name}")
                    stories.extend(result)
        
        logger.info(f"Total government stories collected: {len(stories)}")
        return stories
    
    async def _fetch_government_feed(self, session: aiohttp.ClientSession, 
                                   source_name: str, feed_url: str, 
                                   cutoff_time: datetime) -> List[NewsStory]:
        """Fetch individual government RSS feed"""
        try:
            logger.info(f"Fetching government feed: {source_name} from {feed_url}")
            
            timeout = aiohttp.ClientTimeout(total=30, connect=10)
            async with session.get(feed_url, timeout=timeout, 
                                headers={'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'}) as response:
                if response.status == 200:
                    content = await response.text()
                    stories = self._parse_government_content(content, source_name, cutoff_time)
                    logger.info(f"Successfully parsed {len(stories)} stories from government source {source_name}")
                    return stories
                else:
                    logger.error(f"HTTP error {response.status} for government source {source_name}")
        except Exception as e:
            logger.error(f"Error fetching government source {source_name}: {e}")
        return []
    
    def _parse_government_content(self, content: str, source_name: str, 
                                cutoff_time: datetime) -> List[NewsStory]:
        """Parse government RSS content"""
        import feedparser
        stories = []
        
        try:
            feed = feedparser.parse(content)
            for entry in feed.entries:
                pub_date = self._parse_date(str(entry.get('published', '') or ''))
                if pub_date and pub_date > cutoff_time:
                    story = NewsStory(
                        title=str(entry.get('title', '') or ''),
                        summary=str(entry.get('summary', '') or '')[:200],
                        url=str(entry.get('link', '') or ''),
                        source=f"Government {source_name}",
                        published=pub_date,
                        category='Politics and elections',
                        source_weights=[SOURCE_WEIGHTS.get(f"Government {source_name}", 0.95)]
                    )
                    stories.append(story)
        except Exception as e:
            logging.error(f"Error parsing government content for {source_name}: {e}")
        
        return stories
    
    def _parse_date(self, date_str: str) -> datetime:
        """Parse date from RSS feed"""
        if not date_str:
            return datetime.now(timezone.utc)
        
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(date_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except:
            return datetime.now(timezone.utc)

class AcademicScraper:
    """Scrape academic RSS feeds"""
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Get stories from academic sources"""
        stories = []
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for source_name, feed_url in ACADEMIC_RSS_FEEDS:
                tasks.append(self._fetch_academic_feed(session, source_name, feed_url, cutoff_time))
            
            import asyncio
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                source_name = ACADEMIC_RSS_FEEDS[i][0]
                if isinstance(result, Exception):
                    logging.error(f"Error fetching academic source {source_name}: {result}")
                elif isinstance(result, list):
                    logging.info(f"Collected {len(result)} stories from academic source {source_name}")
                    stories.extend(result)
        
        logging.info(f"Total academic stories collected: {len(stories)}")
        return stories
    
    async def _fetch_academic_feed(self, session: aiohttp.ClientSession, 
                                 source_name: str, feed_url: str, 
                                 cutoff_time: datetime) -> List[NewsStory]:
        """Fetch individual academic RSS feed"""
        try:
            logging.info(f"Fetching academic feed: {source_name} from {feed_url}")
            
            timeout = aiohttp.ClientTimeout(total=30, connect=10)
            async with session.get(feed_url, timeout=timeout, 
                                headers={'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'}) as response:
                if response.status == 200:
                    content = await response.text()
                    stories = self._parse_academic_content(content, source_name, cutoff_time)
                    logging.info(f"Successfully parsed {len(stories)} stories from academic source {source_name}")
                    return stories
                else:
                    logging.error(f"HTTP error {response.status} for academic source {source_name}")
        except Exception as e:
            logging.error(f"Error fetching academic source {source_name}: {e}")
        return []
    
    def _parse_academic_content(self, content: str, source_name: str, 
                              cutoff_time: datetime) -> List[NewsStory]:
        """Parse academic RSS content"""
        import feedparser
        stories = []
        
        try:
            feed = feedparser.parse(content)
            for entry in feed.entries:
                pub_date = self._parse_date(str(entry.get('published', '') or ''))
                if pub_date and pub_date > cutoff_time:
                    story = NewsStory(
                        title=str(entry.get('title', '') or ''),
                        summary=str(entry.get('summary', '') or '')[:200],
                        url=str(entry.get('link', '') or ''),
                        source=f"Academic {source_name}",
                        published=pub_date,
                        category='Business and economy',  # Science/tech category
                        source_weights=[SOURCE_WEIGHTS.get(f"Academic {source_name}", 0.9)]
                    )
                    stories.append(story)
        except Exception as e:
            logging.error(f"Error parsing academic content for {source_name}: {e}")
        
        return stories
    
    def _parse_date(self, date_str: str) -> datetime:
        """Parse date from RSS feed"""
        if not date_str:
            return datetime.now(timezone.utc)
        
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(date_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except:
            return datetime.now(timezone.utc)

class IndustryScraper:
    """Scrape industry RSS feeds"""
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Get stories from industry sources"""
        stories = []
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for source_name, feed_url in INDUSTRY_RSS_FEEDS:
                tasks.append(self._fetch_industry_feed(session, source_name, feed_url, cutoff_time))
            
            import asyncio
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                source_name = INDUSTRY_RSS_FEEDS[i][0]
                if isinstance(result, Exception):
                    logging.error(f"Error fetching industry source {source_name}: {result}")
                elif isinstance(result, list):
                    logging.info(f"Collected {len(result)} stories from industry source {source_name}")
                    stories.extend(result)
        
        logging.info(f"Total industry stories collected: {len(stories)}")
        return stories
    
    async def _fetch_industry_feed(self, session: aiohttp.ClientSession, 
                                 source_name: str, feed_url: str, 
                                 cutoff_time: datetime) -> List[NewsStory]:
        """Fetch individual industry RSS feed"""
        try:
            logging.info(f"Fetching industry feed: {source_name} from {feed_url}")
            
            timeout = aiohttp.ClientTimeout(total=30, connect=10)
            async with session.get(feed_url, timeout=timeout, 
                                headers={'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'}) as response:
                if response.status == 200:
                    content = await response.text()
                    stories = self._parse_industry_content(content, source_name, cutoff_time)
                    logging.info(f"Successfully parsed {len(stories)} stories from industry source {source_name}")
                    return stories
                else:
                    logging.error(f"HTTP error {response.status} for industry source {source_name}")
        except Exception as e:
            logging.error(f"Error fetching industry source {source_name}: {e}")
        return []
    
    def _parse_industry_content(self, content: str, source_name: str, 
                              cutoff_time: datetime) -> List[NewsStory]:
        """Parse industry RSS content"""
        import feedparser
        stories = []
        
        try:
            feed = feedparser.parse(content)
            for entry in feed.entries:
                pub_date = self._parse_date(str(entry.get('published', '') or ''))
                if pub_date and pub_date > cutoff_time:
                    story = NewsStory(
                        title=str(entry.get('title', '') or ''),
                        summary=str(entry.get('summary', '') or '')[:200],
                        url=str(entry.get('link', '') or ''),
                        source=f"Industry {source_name}",
                        published=pub_date,
                        category='Business and economy',
                        source_weights=[SOURCE_WEIGHTS.get(f"Industry {source_name}", 0.7)]
                    )
                    stories.append(story)
        except Exception as e:
            logging.error(f"Error parsing industry content for {source_name}: {e}")
        
        return stories
    
    def _parse_date(self, date_str: str) -> datetime:
        """Parse date from RSS feed"""
        if not date_str:
            return datetime.now(timezone.utc)
        
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(date_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except:
            return datetime.now(timezone.utc) 