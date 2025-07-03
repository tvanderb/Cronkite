# Cronkite News Aggregator - Logging System

## Overview

The Cronkite News Aggregator now features a comprehensive, centralized logging system that provides detailed insights into the news collection and processing pipeline. This system replaces the previous inconsistent logging approach with a unified, configurable logging framework.

## Features

### Centralized Configuration
- **Single Setup Point**: All logging configuration is managed through the `cronkite.__init__` module
- **Configurable Levels**: Support for DEBUG, INFO, WARNING, ERROR, and CRITICAL log levels
- **File and Console Output**: Simultaneous logging to both console and rotating log files
- **Automatic Log Rotation**: Prevents log files from growing too large

### Comprehensive Coverage
- **Story Collection**: Detailed logging of RSS feed fetching, web scraping, and API calls
- **Quality Filtering**: Insights into story filtering decisions and quality metrics
- **Error Handling**: Comprehensive error logging with stack traces
- **Performance Monitoring**: Timing and throughput information
- **Source Diversity**: Geographic and source distribution analysis

### Structured Information
- **Module-Specific Loggers**: Each module has its own logger with descriptive names
- **Consistent Format**: Standardized log message format across all modules
- **Context-Rich Messages**: Logs include relevant metadata (source names, counts, URLs)

## Configuration

### Basic Configuration
Add logging settings to your `config.json`:

```json
{
  "cypher_api_key": "your-api-key",
  "newsapi_key": "your-newsapi-key",
  "hours_back": 24,
  "story_limit": 150,
  "log_level": "INFO",
  "log_file": "logs/cronkite.log",
  "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  "disable_console": false
}
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `log_level` | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| `log_file` | `logs/cronkite.log` | Path to log file (set to `null` to disable file logging) |
| `log_format` | Standard format | Custom log message format string |
| `disable_console` | `false` | If `true`, disable console output (file logging only) |

### Log Levels

- **DEBUG**: Detailed diagnostic information for troubleshooting
- **INFO**: General operational information about the system
- **WARNING**: Indicates a potential problem or unusual situation
- **ERROR**: Indicates a serious problem that prevented normal operation
- **CRITICAL**: Indicates a critical error that may cause the system to fail

## Usage Examples

### Basic Usage
The logging system is automatically initialized when you import the cronkite module:

```python
from cronkite import setup_logging, get_logger

# Get a logger for your module
logger = get_logger(__name__)

# Use the logger
logger.info("Starting news collection")
logger.debug("Processing story: %s", story.title)
logger.error("Failed to fetch RSS feed: %s", error)
```

### Custom Configuration
You can customize logging behavior:

```python
from cronkite import setup_logging

# Configure logging with custom settings
setup_logging(
    log_level="DEBUG",
    log_file="custom_logs/news_aggregator.log",
    log_format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    disable_console=False  # Set to True to disable console output
)
```

### Disable Console Output
To disable logging to STDOUT (console) and only log to file:

```json
{
  "disable_console": true
}
```

Or programmatically:

```python
setup_logging(
    log_file="logs/cronkite.log",
    disable_console=True
)
```

## Log Message Categories

### Story Collection
- RSS feed fetching status and results
- Web scraping attempts and outcomes
- API call responses and errors
- Story parsing and validation

### Quality Processing
- Story filtering decisions
- Quality metrics calculation
- Geographic diversity analysis
- Source reputation scoring

### System Operations
- Application startup and shutdown
- Configuration loading
- Error handling and recovery
- Performance metrics

## Sample Log Output

```
2024-01-15 10:30:15,123 - cronkite - INFO - Starting Cronkite News Aggregator
2024-01-15 10:30:15,124 - cronkite - INFO - Configuration loaded: hours_back=24, story_limit=100
2024-01-15 10:30:15,125 - cronkite - INFO - Initializing news aggregator
2024-01-15 10:30:15,126 - cronkite - INFO - Beginning story collection from all sources
2024-01-15 10:30:15,127 - cronkite.rss - INFO - Fetching RSS feed: BBC World from https://feeds.bbci.co.uk/news/world/rss.xml
2024-01-15 10:30:15,456 - cronkite.rss - INFO - Response status for BBC World: 200
2024-01-15 10:30:15,789 - cronkite.rss - INFO - Successfully parsed 15 stories from BBC World
2024-01-15 10:30:16,123 - cronkite.quality - INFO - Applying quality filters to 150 stories
2024-01-15 10:30:16,456 - cronkite.quality - INFO - Quality filtering complete: 120 stories passed
2024-01-15 10:30:16,789 - cronkite.core - INFO - Final selection: 100 top stories
2024-01-15 10:30:17,123 - cronkite.report - INFO - Generating report for 100 stories
2024-01-15 10:30:20,456 - cronkite.report - INFO - Report generated successfully
2024-01-15 10:30:20,457 - cronkite - INFO - Cronkite News Aggregator execution completed successfully
```

## Troubleshooting

### Common Issues

1. **Log File Not Created**: Ensure the logs directory exists or the parent directory is writable
2. **Too Much Log Output**: Increase the log level to WARNING or ERROR
3. **Missing Log Information**: Decrease the log level to DEBUG
4. **Large Log Files**: The system automatically rotates logs, but you can adjust the `max_bytes` and `backup_count` parameters

### Debug Mode
For detailed troubleshooting, set the log level to DEBUG:

```json
{
  "log_level": "DEBUG"
}
```

This will provide detailed information about:
- Individual story processing
- RSS feed parsing details
- Quality filter decisions
- Network request details

## Best Practices

1. **Use Appropriate Log Levels**: Use DEBUG for detailed troubleshooting, INFO for general operations, ERROR for problems
2. **Include Context**: Log messages should include relevant identifiers (source names, story counts, URLs)
3. **Monitor Log Files**: Regularly check log files for errors or performance issues
4. **Rotate Logs**: The system automatically rotates logs, but monitor disk space usage
5. **Error Handling**: Always log exceptions with full context for debugging

## Integration with Monitoring

The logging system can be easily integrated with external monitoring tools:

- **Log Aggregation**: Send logs to centralized logging systems (ELK, Splunk, etc.)
- **Alerting**: Monitor for ERROR and CRITICAL log levels
- **Metrics**: Parse log messages for performance metrics
- **Audit Trail**: Use logs for compliance and audit purposes

## Performance Considerations

- **Async Logging**: All logging operations are non-blocking
- **Log Rotation**: Automatic rotation prevents disk space issues
- **Configurable Verbosity**: Adjust log levels based on operational needs
- **Library Noise Reduction**: Third-party library logs are filtered to reduce noise 