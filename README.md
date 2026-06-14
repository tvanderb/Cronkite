# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 14, 2026](reports/2026-06-14.md)**

*Last updated: 2026-06-14 13:02 UTC · Generated daily at 6:05 AM EST*

```
2026-06-14  
Armed conflicts and attacks • NSW lifts drone ban over Sydney beach following a shark attack incident (Guardian World) • Ukraine and Moldova begin first phase of EU membership negotiations amid ongoing security concerns (Guardian World) • Zelenskyy thanks UK for intercepting Russian shadow fleet oil tanker in the English Channel (Guardian World) • MPs call for end to real estate event over fears it promotes sale of Israeli settlements (Guardian World) • Australian girl killed in Pakistan after reportedly being shot by police (Guardian World) • Blaze at 1m-sq-ft California warehouse rages into third day (Guardian World) • Deadly Philippines earthquake found to have raised seabed by up to 2 metres (Guardian World) • Trump to meet Mideast partners on sidelines of G7 in France (Bloomberg) • Donald Trump faces a foe he can never defeat: Father Time (Guardian World) • Trump taps lawyer who helped defend him as Wall Street’s top cop (Bloomberg)  
Disasters and accidents • Deadly Philippines earthquake found to have raised seabed by up to 2 metres (Guardian World) • Blaze at 1m-sq-ft California warehouse rages into third day (Guardian World)  
Politics and elections • Farage vows to ban foreign nationals from social housing as byelection looms (Guardian World) • Wes Streeting plans to increase high-skilled immigration if he becomes PM (Guardian World) • UK poised to water down 2030 EV sales targets after industry and union pressure (Guardian World) • Arlette Testyler, rescapée de la rafle du Vél’d’Hiv’en 1942, est morte (Le Monde) • Nicolas Kssis-Martov, historien du sport: « Le football a toujours cristallisé les enjeux politiques de la gauche » (Le Monde) • Trump to meet Mideast partners on sidelines of G7 in France (Bloomberg)  
Law and crime • Australian girl killed in Pakistan after reportedly being shot by police (Guardian World) • Arlette Testyler, rescapée de la rafle du Vél’d’Hiv’en 1942, est morte (Le Monde) • Trump taps lawyer who helped defend him as Wall Street’s top cop (Bloomberg)  
International relations • DNA from 2,000-year-old grape seeds points to origins of modern winemaking (Guardian World) • Ukrainian and Moldovan leaders to enter first phase of EU membership negotiations (Guardian World) • Diplomacy is no longer a safe space for UK’s wounded premier (Bloomberg) • Albaniaans protest against another luxury development on Adriatic coast (Guardian World) • “Straight out of Trumpland”: LGBTQ+ members fight for Pride after Essex library ban (Guardian World) • Trump fête ses 80 ans, son ami Dana White apporte le MMA au cœur de la Maison Blanche (Le Monde) • Présidente 2027: Raphaël Glucksmann fait salle comble aux Docks d’Aubervilliers et se pose en adversaire du RN (Le Monde)  
Business and economy • UK, Japan plan to sign £18 billion clean energy investment deal (Bloomberg)  
Other • UFC to pay White House fighters in crypto issued by Trump company (Guardian World) • Jamaican beach access campaigners go to court to fight privatisation of coast (Guardian World) • Streeting pledges global talent drive, North Sea investment plan (Bloomberg) • “Straight out of Trumpland”: LGBTQ+ members fight for Pride after Essex library ban (Guardian World) • Mourners line Bangkok streets to pay respects to Thailand’s Princess Bha (Guardian World)
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
