import asyncio
import logging
from aggregator.core import NewsAggregator
from aggregator.report import CypherReportGenerator
import json
import os

# Load config from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

# Source weights configuration for aggregation
SOURCE_WEIGHTS = {
    'BBC World': 1.0,
    'Guardian World': 0.9,
    'Reuters World': 0.95,
    'CNN World': 0.85,
    'ABC News': 0.8,
    'NPR World': 0.9,
    'Al Jazeera': 0.85,
    'Reddit r/news': 0.7,
    'Reddit r/worldnews': 0.7,
    'Reddit r/inthenews': 0.6,
    'Reddit r/politics': 0.6,
    'Reddit r/worldpolitics': 0.6,
    'Reddit r/europe': 0.5,
    'Reddit r/uknews': 0.5,
    'Reddit r/usanews': 0.5,
    'Reddit r/science': 0.6,
    'Reddit r/technology': 0.6,
    'Reddit r/environment': 0.5,
    'Reddit r/business': 0.6,
    'Hacker News': 0.6,
    'Mastodon (mastodon.social)': 0.5,
    # Add more sources as needed
}

async def main():
    """Main execution function"""
    logging.basicConfig(level=logging.INFO)
    
    # Initialize aggregator
    aggregator = NewsAggregator()
    
    # Collect stories from all sources
    print("Collecting news stories...")
    stories = await aggregator.collect_all_stories(hours_back=config.get('hours_back', 24), limit=config.get('story_limit', 100))
    print(f"Collected {len(stories)} unique stories")
    
    news_data = aggregator.prepare_for_ingestion()
    
    cypher_generator = CypherReportGenerator(config['cypher_api_key'])
    report = await cypher_generator.generate_report(news_data)
    print(report)

if __name__ == "__main__":
    asyncio.run(main())