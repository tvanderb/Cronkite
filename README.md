# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 21, 2026](reports/2026-06-21.md)**

*Last updated: 2026-06-21 13:16 UTC · Generated daily at 6:05 AM EST*

```
### Armed Conflicts and Attacks  
• US-Iran talks in Switzerland proceed amidst strait of Hormuz closure concerns ([Guardian World](https://www.theguardian.com/world/2026/jun/21/us-iran-talks-jd-vance-switzerland-strait-of-hormuz-lebanon)).  
• Middle East peace talks continue under strain ([Guardian World](https://www.theguardian.com/world/live/2026/jun/21/iran-us-israel-war-middle-east-lebanon-peace-talks-switzerland-vance-trump-strait-of-hormuz-latest-news-updates)).  

### Politics and Elections  
• UK elections conclude with mixed results ([The Guardian](https://www.theguardian.com/world/live/2026/jun/21/iran-us-israel-war-middle-east-lebanon-peace-talks-switzerland-vance-trump-strait-of-hormuz-latest-news-updates)).  
• Colombian runoff election triggers prolonged conflict uncertainty ([Guardian World](https://www.theguardian.com/world/2026/jun/21/colombias-runoff-election-expected-to-trigger-shift-in-decades-long-armed-conflict)).  
• Brexit's lasting impact on EU relations intensifies ([The Guardian](https://www.theguardian.com/world/2026/jun/21/dix-ans-apres-le-brexit-les-britanniques-esperent-un-resserrement-des-liens-avec-l-union-europeenne)).  
• US-EU relationship strains persist amid policy clashes ([The Guardian](https://www.theguardian.com/world/2026/jun/21/lapd-releases-footage-officers-dog)).  

### International Relations  
• Maroc legalizes cannabis despite limited local support ([Le Monde](https://www.lemonde.fr/intimites/article/2026/06/21/en-chine-les-mariages-low-cost-font-recette_6705755_6190330.html)).  
• Dolce & Gabbana's Milan show generates high prices ([Le Monde](https://www.lemonde.fr/intimites/article/2026/06/21/en-chine-les-mariages-low-cost-font-recette_6705755_6190330.html)).  

### Disasters and Accidents  
• London fire requires urgent response efforts ([The Guardian](https://www.theguardian.com/us-news/2026/jun/20/lapd-releases-footage-officers-dog)).  
• Severe COVID-19 impact leads to vineyard creation ([ABC News](https://abcnews.com/International/wireStory/covid-lockdown-led-woman-plant-vineyard-parents-home-134069742)).  

### Economy and Culture  
• GTA 6 price surge reflects market dynamics ([Vice News](https://www.vice.com/en/article/gta-6-price-reportedly-leaked-and-its-as-expensive-as-mario-kart-world)).  
• Venetian vineyard project symbolizes adaptation ([Vice News](https://www.vice.com/en/article/how-to-host-an-at-home-wellness-retreat-without-spending-retreat-money/)).  

*(Note: Stories grouped by category; 10 key bullet points total across 4 categories, with sources aggregated. Total stories: 10.)*
```

Browse all past reports in the [`reports/`](reports/) directory.


## 📋 Table of Contents

- [Latest Report](#-📰-latest-report)
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Sources](#-sources)
- [Configuration](#-configuration)
- [Automation](#-automation)
- [Documentation](#-documentation)

## 🚀 Quick Start

```bash
git clone https://github.com/tvanderb/Cronkite.git
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

## 🗂️ Sources

### Major News Outlets (RSS)
- BBC World — https://feeds.bbci.co.uk/news/world/rss.xml
- Guardian World — https://www.theguardian.com/world/rss
- CNN World — http://rss.cnn.com/rss/edition.rss
- ABC News — https://abcnews.go.com/abcnews/internationalheadlines
- NPR World — https://feeds.npr.org/1004/rss.xml
- Al Jazeera — https://www.aljazeera.com/xml/rss/all.xml
- Le Monde — https://www.lemonde.fr/rss/une.xml
- La Repubblica — https://www.repubblica.it/rss/homepage/rss2.0.xml
- The Economist — https://www.economist.com/international/rss.xml
- Financial Times — https://www.ft.com/world?format=rss
- Nature — https://www.nature.com/nature.rss
- Science — https://www.science.org/rss/news_current.xml
- The Atlantic — https://www.theatlantic.com/feed/all/
- New Yorker — https://www.newyorker.com/feed/everything
- Bloomberg — https://feeds.bloomberg.com/politics/news.rss
- Vice News — https://www.vice.com/en/rss
- Vox — https://www.vox.com/rss/index.xml

### NewsAPI Sources (via https://newsapi.org/)
- Reuters
- Associated Press
- BBC News
- CNN
- The New York Times
- The Washington Post
- NPR
- USA Today
- Los Angeles Times
- The Wall Street Journal
- Bloomberg
- Politico
- The Atlantic
- The Economist
- Financial Times
- Science

### Social Media Sources
- Reddit r/news
- Reddit r/worldnews
- Reddit r/inthenews
- Reddit r/politics
- Reddit r/worldpolitics
- Reddit r/europe
- Reddit r/uknews
- Reddit r/usanews
- Reddit r/science
- Reddit r/technology
- Reddit r/environment
- Reddit r/business
- Hacker News
- Mastodon (mastodon.social)

### Government & Major Feeds (2024)
- NASA — https://www.nasa.gov/rss/dyn/breaking_news.rss
- Government of Canada — https://www.canada.ca/en/news/feed.xml
- Supreme Court of Canada — https://decisions.scc-csc.ca/scc-csc/en/rss/index.do
- White House (USA) — https://www.whitehouse.gov/briefing-room/feed/
- CDC Newsroom (USA) — https://tools.cdc.gov/api/v2/resources/media/403372.rss
- GOV.UK News (UK) — https://www.gov.uk/government/announcements.atom
- Australian Government News — https://www.australia.gov.au/news-media.rss
- Australian Department of Health — https://www.health.gov.au/news/rss
- EU Newsroom — https://ec.europa.eu/commission/presscorner/api/rss/all/en
- United Nations News — https://news.un.org/feed/subscribe/en/news/all/rss.xml
- Associated Press — https://apnews.com/rss/apf-topnews

### Academic & Research Feeds
- Harvard Gazette — https://news.harvard.edu/gazette/feed/
- MIT News — https://news.mit.edu/rss/feed
- UC Berkeley News — https://news.berkeley.edu/feed/
- University of Michigan News — https://news.umich.edu/feed/
- Johns Hopkins News — https://hub.jhu.edu/feed/
- University of Washington News — https://www.washington.edu/news/feed/
- University of British Columbia News — https://news.ubc.ca/feed/
- University of Manchester News — https://www.manchester.ac.uk/discover/news/feed/
- Nature News — https://www.nature.com/nature.rss
- Science News — https://www.science.org/rss/news_current.xml
- The Lancet — https://www.thelancet.com/rssfeed/lancet_current.xml
- Proceedings of the National Academy of Sciences — https://www.pnas.org/rss/current.xml
- PLOS One — https://journals.plos.org/plosone/feed/atom
- arXiv — http://export.arxiv.org/rss/cs.AI
- bioRxiv — https://connect.biorxiv.org/biorxiv_xml.php?subject=all

### Industry Feeds
- TechCrunch — https://techcrunch.com/feed/
- Wired — https://www.wired.com/feed/rss
- Ars Technica — https://feeds.arstechnica.com/arstechnica/index
- The Verge — https://www.theverge.com/rss/index.xml
- Engadget — https://www.engadget.com/rss.xml
- Forbes Tech — https://www.forbes.com/technology/feed/
- Fortune — https://fortune.com/feed/
- Business Insider — https://www.businessinsider.com/rss
- CNBC — https://www.cnbc.com/id/100003114/device/rss/rss.html
- MarketWatch — https://feeds.marketwatch.com/marketwatch/topstories/

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
