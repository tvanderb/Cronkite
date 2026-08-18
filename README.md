# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[August 18, 2026](reports/2026-08-18.md)**

*Last updated: 2026-08-18 11:34 UTC · Generated daily at 6:05 AM EST*

```
August 18, 2026

**Armed conflicts and attacks**
• Oil prices surge as US-Iran ceasefire expires and Trump threatens Oman with military action (Guardian World)
• Russia warns UK of "consequences" over reports Ukraine using British drones in attacks on Russian territory (Guardian World)
• South Korea president calls for military independence following Trump's suggestion to cut joint drills with US (Guardian World)
• Trump's move to reduce South Korea alliance criticized as "inane, haphazard decision" by lawmakers (Guardian World)
• South Korea pushes for nuclear submarine deal after Trump's rebuke (Bloomberg)
• Ebola outbreak in Democratic Republic of Congo becomes deadliest in country's history (Guardian World)
• Russian missiles hit Petchenihy in Kharkiv oblast, killing 10, according to local authorities (Le Monde)
• Russian Supreme Court blocks only anti-war party from running in upcoming elections (Le Monde)
• Hamas accepts US peace roadmap for Gaza; Israel expected to respond on disarmament (Le Monde)
• Iran conflict updates: Araghchi states "Israel is the obstacle to agreement with the USA" (La Repubblica)

**Disasters and accidents**
• Mechanical fault suspected in helicopter crash that killed British newlyweds off Sifnos, Greece (Guardian World)
• South Korea city devastated by nearly one meter of rainfall, triggering deadly landslide (Guardian World)
• Family of missing 18-year-old hiker "absolutely devastated" as search continues in rugged NSW terrain (Guardian World)
• WA police appeal for help locating 10-year-old girl missing from Perth suburbs (Guardian World)

**Politics and elections**
• Trump 2.0 administration has deleted or altered nearly 400 US federal datasets, threatening public health and education data (Guardian World)
• Redistricting disrupts Florida primary as Alaska awaits Dan Sullivan v Dan Sullivan legal battle (Guardian World)
• Top Democrats compete in Florida primary despite lack of progressive platform differences (Guardian World)
• Can Trump's peace plan for Gaza be salvaged? Analysis of current developments (Guardian World)
• Netanyahu and Kushner hold talks without making progress on stalled Gaza agreement (Guardian World)
• Netanyahu party campaign billboard compares opponent Mamdani to Iranian and Hezbollah leaders (Guardian World)
• Myanmar's leader to meet Putin on first Moscow visit as president (Bloomberg)
• Trump threatens to bomb Oman if it interferes with Iran deal as Kushner meets Netanyahu (Guardian World)
• Bondi library removes book "How to Sell a Genocide" from shelves following complaint (Guardian World)

**Law and crime**
• Sydney Swans to sanction players for "serious breach" regarding sexual assault allegations (Guardian World)
• Italian security law criticized after death of Moroccan man in police custody; migration "weaponized" (Guardian World)
• Emergency judge called for Red Cross ambulance driver Luca Spada after deaths in transit (La Repubblica)

**International relations**
• Controversial NDIS bill passes Senate with "substantial" amendments after Labor and Coalition agreement (Guardian World)
• UK pay growth slows as job vacancies reach five-year low amid ongoing geopolitical tensions (Guardian World)
• Governments' borrowing costs hit multi-decade highs as US-Iran peace prospects diminish (Guardian World)
• Fortnite Cube Hours scheduled for Sprite Spree Week (August 18) (Vice News)
• South Korea city deluged by almost one meter of rain, triggering deadly landslide (Guardian World)
• A Gaza family fears settler violence will displace them from West Bank home (NPR World)
• Riyadh creates entirely new public transportation network to transform city commuting (Le Monde)

**Business and economy**
• Overground running incurs higher energetic cost than treadmill running at 1% grade, study finds (PLOS One)
• UK pay growth slows as job vacancies hit five-year low (Guardian World)
• Governments' borrowing costs hit multi-decade highs as US-Iran peace hopes fade (Guardian World)
• British shoppers snap up picnic foods during heatwave; "picky bits" popular (Guardian World)
• SAR11 Genome Atlas published: comprehensive genome and gene catalog for dominant ocean bacterial clade (bioRxiv)
• CRISPR treatment offers new hope after 34 years of sickle cell crises (UC Berkeley News)
• Usher's Atlanta mansion features art collection, hookah lounge, and barbershop (MarketWatch)
• Virgin Trains moves closer to European rail services, challenging Eurostar dominance (Guardian World)

**Environment**
• England's ancient oak trees dying in extreme hot and dry weather conditions (Guardian World)

**Science and technology**
• New genomic atlas reveals SAR11 bacteria genome for ocean ecosystem studies (bioRxiv)
• CRISPR gene editing provides breakthrough treatment for chronic sickle cell disease (UC Berkeley News)

**Culture and entertainment**
• Magic: The Gathering releases five new The Hobbit card drops featuring super rare cards and art (Vice News)
• 3 one-hit wonders from the 1990s who still perform regularly (Vice News)
• Brent Hinds appears on new CKY song, marking first posthumous recording of late Mastodon guitarist (Vice News)
• Drake responds to "Goated" Ella Langly spotted dancing to his song with Lil Wayne (Vice News)

**Human interest**
• Hayden Panettiere, known for "Heroes" and "Nashville," dies at age 36 (Associated Press)
• Usher's Atlanta mansion showcases extensive art collection alongside recreational amenities (MarketWatch)
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
