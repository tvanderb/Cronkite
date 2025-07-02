import aiohttp
import logging
from datetime import datetime
from typing import List, Dict
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .core import NewsStory
from .rss import RSSFeedScraper

class WebScraper:
    """Direct web scraping for sites without good RSS"""
    
    SCRAPE_TARGETS = [
        {
            'name': 'BBC Breaking',
            'url': 'https://www.bbc.com/news',
            'headline_selector': 'h2[data-testid="card-headline"] a',
            'summary_selector': 'p[data-testid="card-description"]'
        },
        {
            'name': 'Reuters Top',
            'url': 'https://www.reuters.com/world/',
            'headline_selector': 'a[data-testid="Heading"]',
            'summary_selector': 'p[data-testid="Body"]'
        }
    ]
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Scrape stories from news websites"""
        stories = []
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for target in self.SCRAPE_TARGETS:
                tasks.append(self._scrape_site(session, target, cutoff_time))
            
            import asyncio
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for result in results:
                if not isinstance(result, Exception):
                    stories.extend(result)
        
        return stories
    
    async def _scrape_site(self, session: aiohttp.ClientSession, 
                          target: Dict, cutoff_time: datetime) -> List[NewsStory]:
        """Scrape individual news site"""
        stories = []
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'}
            from aiohttp import ClientTimeout
            timeout = ClientTimeout(total=15)
            async with session.get(target['url'], headers=headers, timeout=timeout) as response:
                if response.status == 200:
                    html = await response.text()
                    stories = self._parse_html_content(html, target, cutoff_time)
        except Exception as e:
            logging.error(f"Error scraping {target['name']}: {e}")
        return stories
    
    def _parse_html_content(self, html: str, target: Dict, 
                           cutoff_time: datetime) -> List[NewsStory]:
        """Parse HTML content for stories"""
        stories = []
        try:
            soup = BeautifulSoup(html, 'html.parser')
            headlines = soup.select(target['headline_selector'])
            
            for headline in headlines[:20]:  # Limit to top 20
                title = headline.get_text().strip()
                url = headline.get('href', '')
                if url is not None:
                    url = str(url)
                else:
                    url = ''
                
                # Make absolute URL
                if url and isinstance(url, str) and not url.startswith('http'):
                    url = urljoin(target['url'], url)
                
                # Try to find summary (optional)
                summary = ""
                parent = headline.parent
                if parent:
                    summary_elem = parent.find('p') or parent.find_next('p')
                    if summary_elem:
                        summary = summary_elem.get_text().strip()[:200]
                
                if title and url:
                    story = NewsStory(
                        title=title,
                        summary=summary,
                        url=url,
                        source=target['name'],
                        published=datetime.now(),  # Approximate - could enhance
                        category=self._categorize_story(title + ' ' + summary)
                    )
                    stories.append(story)
        except Exception as e:
            logging.error(f"Error parsing HTML for {target['name']}: {e}")
        return stories
    
    def _categorize_story(self, text: str) -> str:
        """Reuse categorization logic from RSS scraper"""
        return RSSFeedScraper()._categorize_story(text) 