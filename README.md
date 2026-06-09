# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 9, 2026](reports/2026-06-09.md)**

*Last updated: 2026-06-09 13:47 UTC · Generated daily at 6:05 AM EST*

```
- **Armed conflicts and attacks**
  • NSW prosecutors launch proceedings against Labor officials accused of disguising donations to Chris Minns (https://www.theguardian.com/australia-news/2026/jun/09/court-proceedings-labor-officials-accused-disguising-chris-minns)
  • Northern Ireland minister urges calm after horrific knife attack in Belfast (https://www.theguardian.com/politics/live/2026/jun/09/labour-badenoch-equality-duty-now-ank-taw-hole-updates)

- **Disasters and accidents**
  • Man seriously injured in Louisiana stabbing Starmer describes it as ‘sickening’ (https://www.theguardian.com/uk-news/2026/jun/09/man-seriously-injured-in-belfast-stabbing-starmer-describes-as-sickening)
  • One woman’s ‘sad nipple syndrome’ experience leads thousands to admit they share the same condition (https://www.vice.com/en/article/one-womans-sad-nipple-syndrome-experience-caused-thousands-to-admit-they-have-the-same-condition)

- **Politics and elections**
  • Former MLB star crashes plane bound for US, killing two pilots (https://www.theguardian.com/us-news/2026/jun/08/us-pilots-killed-plane-bound-to-pick-up-former-mlb-star)
  • Zelenskyy hopes to invite King Charles to Ukraine (https://www.theguardian.com/world/2026/jun/09/zelenskyy-hopes-to-invite-king-charles-state-visit-ukraine)

- **Law and crime**
  • Trump's 'No Tax On Tips' policy fails to sway Nevada voters (https://www.bloomberg.com/news/videos/2026-06-09/trump-s-no-tax-on-tips-isn-t-persuading-nevada-voters)
  • Lawyer sets to testify before House panel on Jeffrey Epstein’s assistant Lesley Groff (https://www.theguardian.com/us-news/2026/jun/09/jeffrey-epstein-assistant-lesley-groff-testifies)

- **International relations**
  • Israel and Iran pause conflict after Trump calls for ceasefire (https://www.le Monde.fr/international/live/2026/06/09/en-direct-guerre-au-moyen-orient-la-ville-de-tyr-dans-le-sud-du-liban-bombardee-par-l-armee-israelienne-au-moins-huit-morts-et-cinq-blesses_6697888_3210.html)
  • US legation in Kabul evacuates diplomats amid growing unrest (https://www.theguardian.com/world/2026/06/08/us-legation-in-kabul-evacuates-diplomats-amid-growing-unrest)

- **Business and economy**
  • Tesla CEO Elon Musk’s company shares soar ahead of expected NBA final (https://www.nasa.gov/centers-and-facilities/johnson/how-nasa-science-and-artemis-are-shaping-the-2026-fifa-world-cup/)
  • Mango sues Australian clothing brand over 'blatant copying' of tabs (https://www.theguardian.com/australia-news/2026/jun/09/levis-sues-successful-tabs-on-pockets)

- **Health and society**
  • UK government urges caution over Gaza strike amid rising casualties (https://www.theguardian.com/world/2026/jun/08/en-direct-guerre-au-moyen-orient-la-ville-de-tyr-dans-le-sud-du-liban-bombardee-par-l-armee-israelienne-au-moins-huit-morts-et-cinq-blesses_6697888_3210.html)
  • Philippines earthquake leaves 37 dead in Mindanao (https://www.theguardian.com/world/2026/jun/08/philippines-earthquake-mindanao-tsunami-warnings)

- **Armed conflicts and attacks**
  • Ukraine: Trump calls for halt to Moscow’s rocket attacks (https://www.lemonde.fr/international/live/2026/06/09/en-direct-guerre-en-ukraine-un-21e-paquet-de-sanctions-contre-la-russie-presente-par-la-presidente-de-la-commission-europeenne-ursula-von-der-leyen_6698620_3210.html)

- **Crime and investigations**
  • Two US pilots killed in plane crash in Dominican Republic (https://www.theguardian.com/us-news/2026/jun/08/us-pilots-killed-plane-crash-dominican-republic)
  • Leading French star Patrick Bruel held by police investigating new sexual assault allegations (https://www.theguardian.com/culture/2026/jun/09/patrick-bruel-french-singer-actor-sexual-assault-allegations-ntwnfb)

- **Technology and media**
  • NASA releases details on NASA’s INCUS satellites progressing toward launch (https://science.nasa.gov/photojournal/nasas-incus-satellites-progress-toward-launch/)
  • Podcast discusses the global crap about the World Cup and cartel profits (https://www.bloomberg.com/news/videos/2026-06-09/the-criminal-cartels-cashing-in-on-the-world-cup-podcast)

- **Politics and elections**
  • Graham Platner’s scandal threatens Democratic primary in Maine (https://www.bloomberg.com/news/articles/2026-06-09/graham-platner-s-scandals-risk-spoiling-democrats-bet-in-maine)

- **Disasters and accidents**
  • Powerful earthquake in southern Philippines kills 37 people (https://www.theguardian.com/world/2026/jun/08/philippines-earthquake-mindanao-tsunami-warnings)

- **Science and innovation**
  • Persona 6 set to release date reported for 2027 (https://www.vice.com/en/article/persona-6-release-date-reportedly-still-planned-for-2027)
  • Mango plans to open 45 new stores in France by 2028, creating 700 jobs (https://www.lemonde.fr/economie/article/2026/06/09/la-marque-de-vetements-mango-veut-ouvrir-45-nouveaux-magasins-en-france-d-ici-a-2028-avec-pres-de-700-emplois-a-la-cle_6700155_3234.html)
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
