import asyncio
import logging
from cronkite.core import NewsAggregator
from cronkite.report import CypherReportGenerator
import json
import os
from cronkite.config import SOURCE_WEIGHTS

# Load config from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

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