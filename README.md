# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 25, 2026](reports/2026-06-25.md)**

*Last updated: 2026-06-25 13:25 UTC · Generated daily at 6:05 AM EST*

```
**Date:June 25, 2026**  

**Armed conflicts and attacks**  
• Venezuela declares a state of emergency after deadly twin earthquakes kill at least 164 people and injure thousands (The Guardian World, Le Monde) ([The Guardian](https://www.theguardian.com/world/2026/jun/25/earthquake-venezuela-caracas-tremors-aftershocks), [Le Monde](https://www.lemonde.fr/international/article/2026/06/25/seismes-au-venezuela-au-moins-164-morts-et-pres-de-1-000-blesses-selon-un-nouveau-bilan-provisoire_6714182_3210.html))  
• Ukraine’s eastern front faces relentless Russian pressure, with fighting reported near Sloviansk and Kramatorsk (Le Monde) ([Le Monde](https://www.lemonde.fr/international/article/2026/06/25/guerre-en-ukraine-de-sloviansk-a-kramatorsk-un-arriere-front-sous-la-pression-constante-des-russes_6713361_3210.html))  
• US Senate rejects an Iran War Powers Resolution, complicating efforts to curb military action against Iran (Bloomberg) ([Bloomberg](https://www.bloomberg.com/news/videos/2026-06-25/us-senate-votes-down-iran-war-powers-resolution-video))  
• A vehicle plows into a crowd in Cabo San Lucas, Mexico, following Mexico’s World Cup victory over Czechia (The Guardian World) ([The Guardian](https://www.theguardian.com/football/2026/jun/25/vehicle-hits-crowd-in-cabo-san-lucas-after-mexicos-world-cup-victory-over-czechia))  
• German defense officials acknowledge significant gaps in military readiness amid rising tensions (Bloomberg) ([Bloomberg](https://www.bloomberg.com/news/videos/2026-06-25/germany-s-defense-sector-has-long-way-to-go-minister-video))  

**Disasters and accidents**  
• Venezuela’s earthquake crisis escalates, with authorities reporting over 1,000 injured (The Guardian World, Le Monde) ([The Guardian](https://www.theguardian.com/world/live/2026/jun/25/venezuela-earthquake-live-updates-quake-aftershocks-terremoto-caracas-latest), [Le Monde](https://www.lemonde.fr/international/article/2026/06/25/seismes-au-venezuela-au-moins-164-morts-et-pres-de-1-000-blesses-selon-un-nouveau-bilan-provisoire_6714182_3210.html))  

**Politics and elections**  
• UK to halve tariff-free steel imports to counter cheap Chinese metal, signaling trade tensions (The Guardian World) ([The Guardian](https://www.theguardian.com/business/2026/jun/25/uk-to-halve-tariff-free-steel-imports-to-counter-glut-of-cheap-chinese-metal))  
• Trump meets with House Speaker to address legislative gridlock, including disputes over housing bills and Supreme Court regulations (The Guardian World) ([The Guardian](https://www.theguardian.com/us-news/live/2026/jun/25/trump-housing-bill-senate-regulations-supreme-court-latest-news-updates))  
• Vietnamese police block roads ahead of an anti-government protest in Kenya’s capital (ABC News) ([ABC News](https://abcnews.com/International/wireStory/kenyan-police-block-roads-countrys-capital-ahead-anti-134195756))  
• Sweden’s opposition argues a bank tax could boost household spending (Bloomberg) ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-25/swedish-opposition-sees-bank-tax-helping-households-spend-more))  

**Law and crime**  
• A tourist sparks a fight after entering a gender-segregated beach in Italy (Vice News) ([Vice News](https://www.vice.com/en/article/tourist-sparks-fight-after-crossing-into-mens-side-of-italys-last-gender-segregated-beach))  
• Brazilian police arrest a Spanish citizen for racism at São Paulo airport (The Guardian World) ([The Guardian](https://www.theguardian.com/world/2026/jun/24/brazilian-police-arrest-spanish-citizen-racism))  
• Pakistan police rescue a French woman and her children held captive by her husband for 12 years (The Guardian World) ([The Guardian](https://www.theguardian.com/world/2026/jun/24/pakistan-police-rescue-french-woman-sylvie-yasmina-children-allegedly-held-captive-husband))  

**International relations**  
• A LEGO car built from 327,906 bricks sets a new speed record (Vice News) ([Vice News](https://www.vice.com/en/article/a-lego-car-made-from-327906-bricks-just-set-a-new-speed-record))  
• NASA shares progress on its Moon Base mission, advancing plans for lunar and Mars exploration (NASA) ([NASA](https://www.nasa.gov/news-release/nasa-to-share-latest-moon-base-mission-progress))  
• Rockstar Games addresses backlash over physical disc distribution for GTA 6 (Vice News) ([Vice News](https://www.vice.com/en/article/rockstar-games-responds-to-gta-6-physical-disc-backlash))  
• Cambodia’s Supreme Court upholds treason convictions of two journalists, raising press freedom concerns (ABC News) ([ABC News](https://abcnews.com/International/wireStory/cambodias-supreme-court-rule-treason-appeal-2-journalists-134192048))  

**Business and economy**  
• UK’s grid operator pays £10 million to secure extra power and avoid a supply crunch during a heatwave (The Guardian World) ([The Guardian](https://www.theguardian.com/business/2026/jun/24/heatwave-great-britain-grid-operator-extra-electricity-power-plants))  
• Oil prices drop to pre-Iran war levels as more tankers exit the Strait of Hormuz (The Guardian World) ([The Guardian](https://www.theguardian.com/business/2026/jun/25/oil-price-falls-pre-iran-war-levels-more-tankers-exit-strait-of-hormuz))  

This report adheres to Legible News’ format, prioritizing significant events, merging duplicates, and ensuring a balanced mix of sources and regions.
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
