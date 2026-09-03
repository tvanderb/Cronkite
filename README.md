# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[September 3, 2026](reports/2026-09-03.md)**

*Last updated: 2026-09-03 14:59 UTC · Generated daily at 6:05 AM EST*

```
September 3, 2026  

**Business and economy**  
• Europe doesn’t need any lessons on growth; Fortune will reveal 500 reasons why on September 16 ([Industry Fortune](https://fortune.com/2026/09/03/september-16-fortune-ceo-forum-500-uk/))  
• Yen surges as markets anticipate a Bank of Japan rate hike ([Guardian World](https://www.theguardian.com/business/2026/sep/03/yen-soars-bank-of-japan-tipped-to-raise-interest-rates))  
• Dutch central bank transfers 86 tonnes of gold to the UK from the US and Canada, citing geopolitical unrest ([Guardian World](https://www.theguardian.com/world/2026/sep/03/netherlands-gold-dutch-central-bank-uk-us-and-canada-geopolitical-unrest))  
• U.S. economy gains momentum as summer ends, but lingering risks remain ([Industry MarketWatch](https://www.marketwatch.com/story/the-u-s-economy-powers-up-as-summer-winds-down-but-its-not-free-of-tripwires-2208ae5a?mod=mw_rss_topstories))  
• Advice column urges men to share household chores, starting with teaching sons to help ([Industry Business Insider](https://www.businessinsider.com/teaching-men-to-clean-asking-son-husband-help-chores-2026-9))  
• UK mortgage holders prepare for higher rates amid a global bond sell‑off ([Guardian World](https://www.theguardian.com/money/2026/sep/03/uk-mortgage-borrowers-brace-for-rate-jump-global-bond-sell-off))  
• John Lewis to launch a YouTube chat‑show aimed at improving AI‑driven search results ([Guardian World](https://www.theguardian.com/business/2026/sep/03/john-lewis-youtube-chat-show-angela-scanlon))  
• Apple Maps renames Lake Ontario as “Lake America” for U.S. users following a Trump executive order ([Guardian World](https://www.theguardian.com/technology/2026/sep/02/apple-maps-renames-lake-ontario-lake-america))  
• New University of Washington research shows the Arctic melt season is now a week longer than in the 1980s ([Academic University of Washington News](https://www.washington.edu/news/2026/09/02/qa-the-arctic-melt-season-is-a-week-longer-now-than-it-was-in-the-1980s-shows-new-uw-research-on-sea-ice-trends/))  

**Politics and elections**  
• Swedish opposition parties pledge to assist Britons facing deportation if they gain power ([Guardian World](https://www.theguardian.com/world/2026/sep/03/swedish-mp-promises-help-for-britons-facing-deportation-if-his-party-wins-power-general-election))  
• Wife of a British man threatened with deportation from Sweden urges Andy Burnham to intervene ([Guardian World](https://www.theguardian.com/world/2026/sep/03/wife-of-british-man-at-risk-of-deportation-from-sweden-calls-on-burnham-to-intervene))  
• Kemi Badenoch denounces Reform UK’s proposed press bans as “authoritarian” in live UK politics coverage ([Guardian World](https://www.theguardian.com/politics/live/2026/sep/03/andy-burnham-emmanuel-macron-zack-polanski-latest-news-updates))  
• Hong Kong court upholds convictions of Cardinal Joseph Zen and others related to a protester relief fund ([ABC News](https://abcnews.com/International/wireStory/hong-kong-court-upholds-convictions-cardinal-joseph-zen-136163714))  
• La Repubblica publishes the (now‑deleted) interview with Ranucci and Lavitola on Zimbabwe and carbon credits ([La Repubblica](https://roma.repubblica.it/cronaca/2026/09/03/news/ranucci_lavitola_intervista_zimbabwe_carbon_credit-42556253
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
- Der Spiegel — https://www.spiegel.de/international/index.rss
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

### Government & Major Feeds
- NASA — https://www.nasa.gov/feed/
- GOV.UK News (UK) — https://www.gov.uk/search/news-and-communications.atom
- EU Newsroom — https://ec.europa.eu/commission/presscorner/api/rss?language=en
- United Nations News — https://news.un.org/feed/subscribe/en/news/all/rss.xml

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
- arXiv — https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=25
- bioRxiv — https://connect.biorxiv.org/biorxiv_xml.php?subject=all

### Industry Feeds
- TechCrunch — https://techcrunch.com/feed/
- Wired — https://www.wired.com/feed/rss
- Ars Technica — https://feeds.arstechnica.com/arstechnica/index
- The Verge — https://www.theverge.com/rss/index.xml
- Engadget — https://www.engadget.com/rss.xml
- Forbes Innovation — https://www.forbes.com/innovation/feed/
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
