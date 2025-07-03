# Cronkite News Aggregator

Automated news aggregation system that collects, filters, and generates daily reports from multiple sources.

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-03 05:07 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
July 3, 2025...
...
Armed conflicts and attacks...
• The US has halted shipments of Patriot air defense systems and other precision weapons to Ukraine due to low stockpiles, raising concerns in Kyiv (Guardian, Le Monde). ...
• Israel used a 500lb bomb in a strike on a Gaza cafe, killing dozens and prompting accusations of a potential war crime (Guardian). ...
• A Chinese PLA landing ship was spotted unusually close to northern Taiwan ahead of the island's major military exercise, raising tensions (SCMP)....
```

### 📥 Download
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-5-d1cf138b388360bef188b5f9cffce4a6c3589596` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-{number}` artifact

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/news-aggregator.git
cd news-aggregator
pip install -r requirements.txt
cp config.example.json config.json
# Edit config.json with your API keys
python cronkite.py
```

## ✨ Features

- **Multi-source aggregation** (RSS, social media, APIs)
- **Quality filtering** with source reputation scoring
- **Geographic diversity** analysis
- **Automated daily reports** via GitHub Actions
- **Comprehensive logging** system

## ⚙️ Configuration

Required API keys:
- [OpenRouter Cypher](https://openrouter.ai/) - Report generation
- [NewsAPI](https://newsapi.org/) - Additional news sources

```json
{
  "cypher_api_key": "your_key",
  "newsapi_key": "your_key",
  "hours_back": 24,
  "story_limit": 150
}
```

## 🤖 Automation

GitHub Actions automatically generate daily reports:
- **Schedule**: 6:05 AM EST daily
- **Output**: Downloadable news report artifact
- **Setup**: See [GitHub Actions Setup](GITHUB_ACTIONS_SETUP.md)

## 📚 Documentation

- [Logging System](LOGGING.md) - Logging configuration and usage
- [GitHub Actions Setup](GITHUB_ACTIONS_SETUP.md) - Automated workflow setup
- [Configuration Guide](config.example.json) - Example configuration
