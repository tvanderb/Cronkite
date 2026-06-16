# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 16, 2026](reports/2026-06-16.md)**

*Last updated: 2026-06-16 16:02 UTC · Generated daily at 6:05 AM EST*

```
- **Armed conflicts and attacks**
  • Russia’s frigate reportedly fired warning shots at a British yacht in the Channel, sparking international reactions ([Guardian World](https://www.theguardian.com/uk-news/2026/jun/16/russian-frigate-fires-warning-shots-at-british-yacht-in-channel-reports))
  • The incident draws attention from global leaders, with some expressing concern over potential escalation ([Le Monde](https://www.lemonde.fr/international/live/2026/06/16/en-direct-guerre-en-ukraine-un-navire-de-guerre-russe-a-tire-des-coups-de-semonce-en-direction-d-un-bateau-dans-la-manche_6702230_3210.html))

- **Disasters and accidents**
  • A 15-year-old Kenyan student fell 15 floors and died while working at a Sydney hotel; her family is seeking answers ([Guardian World](https://www.theguardian.com/australia-news/2026/jun/17/kenyan-student-sheila-chebii-death-sydney-hotel-meriton-suites-ntwnfb))
  • A Starbucks store in Korea closed temporarily after a mishap during a promotion, prompting public outrage ([Guardian World](https://www.theguardian.com/world/2026/jun/15/starbucks-korea-shut-all-stores-tank-day-promotion))

- **Politics and elections**
  • With the US Senate preparing for a deal signing, both sides claim victory in the agreement ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/us-iran-prepare-for-deal-signing-with-both-claiming-win-video))
  • The UK government is conducting a thorough investigation into a recent attack involving a Russian warship in the English Channel ([Le Monde](https://www.lemonde.fr/international/live/2026/06/16/en-direct-guerre-en-ukraine-un-navire-de-guerre-russe-a-tire-des-coups-de-semonce-en-direction-d-un-bateau-dans-la-manche_6702230_3210.html))
  • The EU seeks to close a gap in US military cuts in Europe, highlighting the importance of transatlantic cooperation ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/nato-seeks-to-make-up-shortfall-of-us-military-cuts-in-europe))

- **Law and crime**
  • An Australian student died after falling 15 floors while working at a hotel in Kenya; authorities are investigating the circumstances ([Guardian World](https://www.theguardian.com/world/2026/jun/17/kenyan-student-sheila-chebii-death-kps))
  • A Russian artist and critic of Vladimir Putin was shot dead in Pakistan, intensifying international scrutiny of the regime ([Guardian World](https://www.theguardian.com/world/2026/jun/16/russia-artist-putin-critic-robert-kuzovkov-shot-dead-poland))

- **International relations**
  • The Guardian reports a potential deal between the US and Iran for a peace agreement, despite both claiming victory ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/us-iran-prepare-for-deal-signing-with-both-claiming-win-video))
  • A live-action version of *Beavis and Butt-Head* is rumored to be in development, with wild casting rumors ([Vice News](https://www.vice.com/en/article/a-live-action-beavis-and-butt-head-movie-almost-happened-and-the-rumored-cast-guidance))
  • The Maldives is considering a controversial “Copper Valley” project as a response to rising copper prices on the Warsaw Bourse ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/poland-floats-copper-valley-idea-as-lumina-metals-gains-on-warsaw-bourse-debut))

- **Disasters and accidents**
  • A luxury steam machine benchmarks leak reported to cause concern over performance ([Vice News](https://www.vice.com/en/article/steam-machine-benchmarks-reportedly-leak-and-spark-concern-over-performance))
  • The UK parliament explores voting on a new law regarding the cost of luxury items, as both parties claim to have passed it ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/nato-seeks-to-make-up-shortfall-of-us-military-cuts-in-europe))

- **Crime and violence**
  • The UK government is investigating the shooting of a Kenyan student while she was visiting a hotel in Pakistan; authorities are urging the public to remain vigilant ([Guardian World](https://www.theguardian.com/world/2026/jun/17/kenyan-student-sheila-chebii-death-pakistan-hania-ahmed-police-ntwnfb))
  • A South African jazz pianist is buried at age 91 amid controversy over a recent death [The Guardian](https://www.theguardian.com/music/2026/jun/15/pianist-abdullah-ibrahim-dies)

- **Education and academic issues**
  • A teacher in Paris is under scrutiny after allegedly relaxing charges against a former elementary school principal [Le Monde](https://www.lemonde.fr/societe/article/2026/06/16/periscolaire-a-paris-pourquoi-un-ex-animateur-de-l-ecole-elementaire-titon-a-ete-relaxe-d-accusations-de-harcelement-sexuel-sur-des-eleves-de-cm1_6703875_3224.html)
  • A French political leader is demanding justice after being shot by police while visiting Pakistan [The Guardian](https://www.theguardian.com/world/2026/jun/16/australian-girl-shot-killed-pakistan-hania-ahmed-police-ntwnfb)

- **War and conflict**
  • France anticipates a heatwave with temperatures potentially reaching 40°C locally by Friday, with Paris expected to exceed 35°C on Thursday and Friday ([Le Monde](https://www.lemonde.fr/planete/article/2026/06/16/vague-de-chaleur-meteo-france-anticipe-des-pointes-a-40-c-localement-en-fin-de-semaine_6703866_3244.html))
  • Zelenskyy praised G7 leaders for their strong ideas on forcing Russia into peace as the conflict in Ukraine continues ([Guardian World](https://www.theguardian.com/world/live/2026/06/16/g7-world-leaders-ukraine-russia-war-iran-trump-zelenskyy-putin-eu-france-eu-europe-latest-news-updates))

Let me know if you need even more stories organized by category!
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
