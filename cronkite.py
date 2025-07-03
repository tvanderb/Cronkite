import asyncio
import json
import os
from cronkite.core import NewsAggregator
from cronkite.report import CypherReportGenerator
from cronkite import setup_logging, get_logger
from cronkite.config import SOURCE_WEIGHTS

# Set up logging
logger = get_logger(__name__)

# Load config from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

async def main():
    """Main execution function"""
    # Configure logging based on config
    log_level = config.get('log_level', 'INFO')
    log_file = config.get('log_file', 'logs/cronkite.log')
    disable_console = config.get('disable_console', False)
    
    setup_logging(
        log_level=log_level,
        log_file=log_file,
        log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        disable_console=disable_console
    )
    
    logger.info("Starting Cronkite News Aggregator")
    logger.info(f"Configuration loaded: hours_back={config.get('hours_back', 24)}, story_limit={config.get('story_limit', 100)}")
    
    # Initialize aggregator
    logger.info("Initializing news aggregator")
    aggregator = NewsAggregator()
    
    # Collect stories from all sources
    logger.info("Beginning story collection from all sources")
    stories = await aggregator.collect_all_stories(
        hours_back=config.get('hours_back', 24), 
        limit=config.get('story_limit', 100)
    )
    logger.info(f"Story collection complete: {len(stories)} unique stories collected")
    
    # Prepare data for report generation
    logger.info("Preparing news data for report generation")
    news_data = aggregator.prepare_for_ingestion()
    
    # Generate report
    logger.info("Generating final report using Cypher Alpha")
    cypher_generator = CypherReportGenerator(config['cypher_api_key'])
    report = await cypher_generator.generate_report(news_data)
    
    logger.info("Report generation complete")
    print(report)  # Keep this print for the final output
    logger.info("Cronkite News Aggregator execution completed successfully")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error during execution: {e}", exc_info=True)
        raise