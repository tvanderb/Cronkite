# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 6, 2026](reports/2026-06-06.md)**

*Last updated: 2026-06-06 12:12 UTC · Generated daily at 6:05 AM EST*

```
• **Armed conflicts and attacks: New definition of obesity announced** – A new international definition of obesity is emerging, with widespread implications for public health. (Vice News)
  - Source: [Vice News](https://www.vice.com/en/article/theres-a-new-definition-of-obesity-and-a-good-chance-it-now-includes-you/)

• **Armed conflicts and attacks: Ukraine crisis intensifies** – Russia claims it has intercepted 86 drones near Saint Petersburg, raising tensions. (Le Monde)
  - Source: [Le Monde](https://www.lemonde.fr/international/live/2026/06/06/en-direct-guerre-en-ukraine-trois-morts-dans-des-attaques-de-drones-russes-dans-l-est-du-pays-la-russie-dit-avoir-intercepte-86-engins_6695365_3210.html)

• **Armed conflicts and attacks: Iran considers peace deal risky** – Iran considers concessions in a peace deal as perilous, per recent reports. (Le Monde)
  - Source: [Le Monde](https://www.lemonde.fr/international/article/2026/06/06/blackouts-hyperinflation-dissent-iran-considers-perilous-prospect-of-peace_6698083_3210.html)

• **Armed conflicts and attacks: Israel strikes Lebanon** – Israel launches attacks on southern Lebanon following evacuations of nine villages. (Guardian World)
  - Source: [Guardian World](https://www.theguardian.com/world/2026/jun/05/israel-strikes-southern-lebanon-evacuations-nine-villages)

• **Armed conflicts and attacks: North Korea unveils new warship** – North Korea unveils a new warship ahead of a visit by Chinese leader Xi. (ABC News)
  - Source: [ABC News](https://abcnews.com/International/wireStory/north-korean-leader-kim-showcases-new-warship-ahead-133638097)

• **Politics and elections: US faces domestic unrest over rising prices** – Rising prices and inflation have led to protests and political tension in the US. (The Guardian)
  - Source: [The Guardian](https://www.theguardian.com/business/2026/06/05/boushey-discusses-jobs-report-wages-and-inflation)

• **Politics and elections: EU strikes over Ukraine deal** – EU nations urge caution and seek compromise in the ongoing Ukraine peace negotiations. (The Guardian)
  - Source: [The Guardian](https://www.theguardian.com/world/2026/jun/06/en-direct-guerre-en-ukraine-trois-morts-dans-des-attaques-de-drones-russes-dans-l-est-du-pays-la-russie-dit-avoir-intercepte-86-engins_6695365_3210.html)

• **Law and crime: Tragedy linked to controversial medical prescribing** – A US coroner finds doctors played a direct role in two deaths through "grossly irresponsible prescribing." (The Guardian)
  - Source: [The Guardian](https://www.theguardian.com/australia-news/2026/jun/06/doctors-grossly-irresponsible-prescribing-played-direct-role-in-two-deaths)

• **Disasters and accidents: NASA tests supersonic X-59 aircraft** – NASA successfully tests the X-59 aircraft for the first time, aiming to reduce sonic booms. (NASA)
  - Source: [NASA](https://www.nasa.gov/aeronautics/x-59-aircraft-flies-supersonic-for-first-time)

• **Politics and elections: Pope calls for secular Spain** – Pope declares the need to modernize Spain to address its complex Catholic legacy. (ABC News)
  - Source: [ABC News](https://abcnews.com/International/wireStory/pope-find-secularized-polarized-spain-catholic-church-complex_6698115_3224.html)

• **Disasters and accidents: US continues to face severe hurricane threats** – US faces near 1,000 Hormuz Strait crossings amid ongoing tensions. (Bloomberg)
  - Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-05/us-forces-see-nearly-1-000-hormuz-crossings-since-ceasefire)

• **Politics and elections: US threats to reconsider role in Bosnia-Hertzburg** – US expresses concerns over its future role in Bosnia amid European rift. (The Guardian)
  - Source: [The Guardian](https://www.theguardian.com/world/2026/jun/06/us-threatens-to-reconsider-role-in-bosnia-and-herzegovina-amid-rift-with-europe)

• **International relations: Armenian elections amid Russian pressure** – Armenia faces pressure from Russia ahead of elections, amid ongoing geopolitical tensions. (Guardian World)
  - Source: [Guardian World](https://www.theguardian.com/world/2026/jun/06/russia-putin-armenia-election)

• **International relations: Pope and global hunger** – WFP highlights global hunger crisis, with focus on Middle East and refugee situations. (Bloomberg)
  - Source: [Bloomberg](https://www.bloomberg.com/news/videos/2026-06-05/wfp-s-skau-on-middle-east-crisis-and-global-hunger-video)

• **Law and crime: Seizure of military equipment by police** – Australian police seize nearly 1,000 Hormuz Strait crossings since a ceasefire. (Bloomberg)
  - Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-05/us-forces-see-nearly-1-000-hormuz-crossings-since-ceasefire)

• **Disasters and accidents: Pope addresses France’s political climate** – Pope announces plans to reshape France’s political landscape. (Le Monde)
  - Source: [Le Monde](https://www.lemonde.fr/disparitions/article/2026/06/06/bernadette-chirac-ancienne-premiere-dame-est-morte-a-l-age-de-93-ans_6698105_3382.html)

• **International relations: Caroline Kovacs on AI and US-Israel tensions** – US tech leader warns of risks from AI developments in the Pentagon. (Bloomberg)
  - Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-05/trump-signs-ai-memo-addressing-issues-in-anthropic-pentagon-feud)

• **Disasters and accidents: UK government names Bernadette Chirac as former First Dame** – UK honors former French First Dame Bernadette Chirac for her advocacy. (Le Monde)
  - Source: [Le Monde](https://www.lemonde.fr/disparitions/article/2026/06/06/bernadette-chirac-ancienne-premiere-dame-est-morte-a-l-age-de-93-ans_6698105_3382.html)
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
