# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[July 13, 2026](reports/2026-07-13.md)**

*Last updated: 2026-07-13 13:28 UTC · Generated daily at 6:05 AM EST*

```
July 13, 2026

**Armed conflicts and attacks**
• US and Iran exchange fire amid escalating tensions over the Strait of Hormuz, with both sides claiming control of the vital shipping route [Bloomberg, Guardian World]
• Iran launches retaliatory strikes following fresh US airstrikes, with Tehran stating attacks render diplomacy futile [Guardian World]
• Houthi forces in Yemen seize a Red Cross medical convoy, taking pilots hostage amid ongoing regional conflict [La Repubblica]
• UK officially lists Iran's Islamic Revolutionary Guard Corps (IRGC) as a terrorist organization in response to regional tensions [Guardian World]
• Wildfires rage in France's Fontainebleau forest and near Paris, prompting emergency responses and cultural site closures [Le Monde, Guardian World]
• Firefighting aircraft deployed from southern France tackle massive blaze near Paris in Fontainebleau region [Guardian World]
• Temperatures soar in the Italian Alps, leading to climbing guide protests and route blockades on the Cervino mountain [La Repubblica]
• Major wildfire burns 800 hectares in Fontainebleau forest, forcing closure of multiple sectors during heat wave [Le Monde]

**Politics and elections**
• Senator Lindsey Graham's sudden death triggers urgent scramble to replace him as Congress reconvenes, with key Republican and Democratic maneuvers underway [Guardian World, Bloomberg]
• European Commission President Ursula von der Leyen proposes EU-wide ban on social media access for children under 13, outlining new child safety measures [Guardian World]
• President Zelenskyy removes Prime Minister as allied leaders convene emergency summit in Paris to address Ukrainian crisis [Bloomberg]
• Swedish MEP files police complaint against Danish colleague for alleged racist hate speech during parliamentary proceedings [Guardian World]
• Pension reforms announced in UK with timeline for "biggest generational changes," affecting millions of savers [GOV.UK]
• French political campaign for 2027 elections officially begins with distinct messaging strategy emerging [La Repubblica]

**Law and crime**
• More than 120 families contacted as police investigate alleged abuse by Sydney childcare worker, expanding criminal probe [Guardian World]
• UNSW academic subjected to Nazi salutes in classroom setting, prompting investigation by antisemitism commission [Guardian World]
• Singapore court postpones French teenager's notorious straw-licking case to July 30, continuing high-profile legal saga [Bloomberg]
• Keystone pipeline operator agrees to $26.9 million penalty settlement over 2024 Kansas oil spill incident [Guardian World]

**Disasters and accidents**
• At least 27 killed and 22 critically injured in devastating fire at Bangkok pub, with authorities investigating cause [Guardian World]
• Fire claims life of British tourist in Andalusian blaze, bringing death toll to 13 as incident stabilizes [Le Monde]

**International relations**
• EU pledges comprehensive social media restrictions for minors, with von der Leyen announcing child protection initiatives [Guardian World]
• Queensland tribunal finds state unlawfully detained children in adult watch houses without proper sanitation facilities [Guardian World]
• Body language expert analyzes Argentina's political shift as Milei's influence wanes, exploring potential third-way governance [Bloomberg]
• Ongoing wildfires across Europe intensify as extreme heat waves fuel blazes in multiple countries [Guardian World, Le Monde]
• TSMC sales surge amid Middle East crisis, with fresh US-Iran strikes threatening regional stability and trade routes [Bloomberg]
• French artists appeal to Macron over severe budget cuts to cultural sector, calling for urgent intervention [Le Monde]
• Italy's political landscape heats up with 2027 election campaign officially commencing under new slogan [La Repubblica]
• Macron's decade-long military relationship characterized by mutual distrust and unresolved tensions [Le Monde]

**Business and economy**
• Morgan Stanley's $2.5 billion parking meter asset sale creates controversy in Chicago city council proceedings [Bloomberg]
• California lawmakers push legislative fix for Hollywood film tax credit program facing budgetary challenges [Bloomberg]
• Study examines socioeconomic factors affecting early breastfeeding initiation in Bangladesh using 2022 demographic health survey data [PLOS One]
• Research explores RNA polymerase III elongation complex dynamics with implications for cellular function [PNAS]
• Scientific investigation reveals cervical spine development mechanisms in yeast gametes affecting gene expression evolution [PNAS]
• Economic analysis examines information choice behavior moderated by user credibility factors [PLOS One]
• Pension scheme rankings undergo dramatic shifts as UK government implements sweeping reforms [GOV.UK]
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
