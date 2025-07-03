import aiohttp
from datetime import datetime, timezone
from typing import List
from .core import NewsStory
from .rss import RSSFeedScraper
from cronkite.config import SOURCE_WEIGHTS
from cronkite import get_logger

logger = get_logger(__name__)

class SocialMediaScraper:
    """Scrape public social media feeds and Reddit"""
    
    async def get_stories(self, cutoff_time: datetime) -> List[NewsStory]:
        """Get stories from social media sources"""
        stories = []
        
        # List of subreddits to scrape
        subreddits = [
            ('news', 'Reddit r/news'),
            ('worldnews', 'Reddit r/worldnews'),
            ('inthenews', 'Reddit r/inthenews'),
            ('politics', 'Reddit r/politics'),
            ('worldpolitics', 'Reddit r/worldpolitics'),
            ('europe', 'Reddit r/europe'),
            ('uknews', 'Reddit r/uknews'),
            ('usanews', 'Reddit r/usanews'),
            ('science', 'Reddit r/science'),
            ('technology', 'Reddit r/technology'),
            ('environment', 'Reddit r/environment'),
            ('business', 'Reddit r/business'),
        ]
        for subreddit, source_name in subreddits:
            subreddit_stories = await self._scrape_subreddit(subreddit, source_name, cutoff_time)
            logger.info(f"Collected {len(subreddit_stories)} stories from {source_name}")
            stories.extend(subreddit_stories)
        
        # Scrape Hacker News
        hn_stories = await self._scrape_hackernews(cutoff_time)
        logger.info(f"Collected {len(hn_stories)} stories from Hacker News")
        stories.extend(hn_stories)
        
        # Scrape Mastodon
        mastodon_stories = await self._scrape_mastodon(cutoff_time)
        logger.info(f"Collected {len(mastodon_stories)} stories from Mastodon (mastodon.social)")
        stories.extend(mastodon_stories)
        
        # Could add Twitter/X scraping here if needed
        # twitter_stories = await self._scrape_twitter_feeds(cutoff_time)
        # stories.extend(twitter_stories)
        
        return stories
    
    async def _scrape_subreddit(self, subreddit: str, source_name: str, cutoff_time: datetime) -> List[NewsStory]:
        """Scrape a given subreddit for recent top posts"""
        stories = []
        try:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=25'
            headers = {'User-Agent': 'NewsAggregator/1.0'}
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        for post in data['data']['children']:
                            post_data = post['data']
                            created_time = datetime.fromtimestamp(post_data['created_utc'], tz=timezone.utc)
                            if created_time > cutoff_time and not post_data.get('is_self', False):
                                story = NewsStory(
                                    title=post_data['title'],
                                    summary=post_data.get('selftext', '')[:200],
                                    url=post_data.get('url', ''),
                                    source=source_name,
                                    published=created_time,
                                    category=self._categorize_story(post_data['title']),
                                    source_weights=[SOURCE_WEIGHTS.get(source_name, 0.5)],
                                    reddit_flair=post_data.get('link_flair_text', '')
                                )
                                stories.append(story)
            logger.info(f"Scraped {len(stories)} stories from /r/{subreddit}")
        except Exception as e:
            logger.error(f"Error scraping subreddit {subreddit}: {e}")
        return stories
    
    def _categorize_story(self, text: str) -> str:
        """Reuse categorization logic"""
        return RSSFeedScraper()._categorize_story(text)

    async def _scrape_hackernews(self, cutoff_time: datetime) -> List[NewsStory]:
        """Scrape top Hacker News stories with external links"""
        stories = []
        try:
            import time
            url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        ids = await resp.json()
                        # Limit to first 50 for efficiency
                        ids = ids[:50]
                        for story_id in ids:
                            item_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
                            async with session.get(item_url) as item_resp:
                                if item_resp.status == 200:
                                    item = await item_resp.json()
                                    # Only include stories with a url and recent
                                    if item and 'url' in item and 'title' in item and 'time' in item:
                                        created_time = datetime.fromtimestamp(item['time'], tz=timezone.utc)
                                        if created_time > cutoff_time:
                                            story = NewsStory(
                                                title=item['title'],
                                                summary='',
                                                url=item['url'],
                                                source='Hacker News',
                                                published=created_time,
                                                category='Business and economy',  # HN is mostly tech/business
                                                source_weights=[SOURCE_WEIGHTS.get('Hacker News', 0.6)]
                                            )
                                            stories.append(story)
            logger.info(f"Scraped {len(stories)} stories from Hacker News")
        except Exception as e:
            logger.error(f"Error scraping Hacker News: {e}")
        return stories

    async def _scrape_mastodon(self, cutoff_time: datetime) -> List[NewsStory]:
        """Scrape public posts from Mastodon (mastodon.social timeline)"""
        stories = []
        try:
            # Public timeline endpoint (no auth needed for public)
            url = 'https://mastodon.social/api/v1/timelines/public?limit=40'
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        posts = await resp.json()
                        for post in posts:
                            # Only include posts with a url, created_at, and English content
                            created_time = None
                            try:
                                created_time = datetime.fromisoformat(post['created_at'].replace('Z', '+00:00'))
                            except Exception:
                                continue
                            if created_time > cutoff_time and post.get('url') and post.get('content'):
                                # Simple English filter
                                if post.get('language') and post['language'] != 'en':
                                    continue
                                # Remove HTML tags from content
                                from bs4 import BeautifulSoup
                                summary = BeautifulSoup(post['content'], 'html.parser').get_text()[:200]
                                story = NewsStory(
                                    title=summary[:80] + '...' if len(summary) > 80 else summary,
                                    summary=summary,
                                    url=post['url'],
                                    source='Mastodon (mastodon.social)',
                                    published=created_time,
                                    category='International relations',
                                    source_weights=[SOURCE_WEIGHTS.get('Mastodon (mastodon.social)', 0.5)]
                                )
                                stories.append(story)
            logger.info(f"Scraped {len(stories)} stories from Mastodon (mastodon.social)")
        except Exception as e:
            logger.error(f"Error scraping Mastodon: {e}")
        return stories 