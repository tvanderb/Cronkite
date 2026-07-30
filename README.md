# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[July 30, 2026](reports/2026-07-30.md)**

*Last updated: 2026-07-30 12:50 UTC · Generated daily at 6:05 AM EST*

```
July 30, 2026

Armed conflicts and attacks
• US launches new wave of strikes against Iran targets overnight, with analysts warning region has entered "uncharted territory" following US-Saudi attacks in Iraq ([Guardian World], [Bloomberg])
• US hits dozens of targets in Iran overnight as peace efforts under threat ([Guardian World])
• Record absence of Cameroon President Paul Biya reignites health speculation amid ongoing political tensions ([Guardian World])
• Ukraine war: unidentified object crashes in Poland, President Tusk suggests it may be Russian missile ([La Repubblica])
• Defence firms see profit boosts as governments increase military spending ([Guardian World])
• EU to provide nearly €3.5 billion additional aid to Ukraine to strengthen military capabilities ([Le Monde])

Disasters and accidents
• Death toll in Japan earthquake rises to at least 34 as heat and aftershocks hamper rescue operations ([Le Monde], [Guardian World])
• Rescue teams face "race against time" searching for trapped survivors as Japan earthquake death toll reaches 13 ([Guardian World])
• Two days after Japan earthquake, at least 34 dead, thousands of survivors, rescue operations hampered by heatwave ([Le Monde])
• Four people found dead on small boats after attempting Channel crossing ([Guardian World])
• Major incident declared as 90 firefighters tackle Suffolk heath wildfire ([Guardian World])
• Firefighters race to extinguish blazes across EU as fire weather breaks records ([Guardian World])
• Families displaced from billionaire-owned London tower after suffering without air conditioning during heatwave ([Guardian World])

Politics and elections
• UK and Spain foreign ministers issue joint statement on wildfires and climate action ([GOV.UK])
• UK and France foreign ministers issue joint statement on wildfires and climate action ([GOV.UK])
• Bank of England holds key interest rate at 3.75% for fifth consecutive time this year ([ABC News], [Guardian World])
• EU launches AI Gigafactories initiative to boost Europe's computing capacity with over €30 billion in investment ([EU Newsroom])
• German Chancellor selects papal encyclical as beach reading amid political challenges ([Guardian World])
• Belgian writer Raoul Vaneigem, known for lyrical resistance to commercial society, dies ([Le Monde])

Law and crime
• Airbus fined £6.4 million for breaching export rules regarding sensitive technology ([Guardian World])
• Kumanjayi Little Baby murder trial delayed until December ([Guardian World])
• Grant writing coaching groups study shows coaching improves proposal submission and success rates ([bioRxiv])
• NSW to deploy paramedics rather than police to certain mental health emergencies following multiple deaths ([Guardian World])
• Police funding gaps and political corruption highlighted in Indian series "Delhi Crime" ([Le Monde])

International relations
• EU wildfires intensify as extreme heat triggers red alert warnings across Europe ([La Repubblica])
• Heatwave prompts government promise fulfillment of 33,000 air conditioners for hospitals and care homes ([Le Monde])
• Europe's industries unprepared for new climate crises according to economic analysis ([Le Monde])
• Global democracy map shows declining freedoms worldwide ([La Repubblica])
• Ferrari Luce subscription model sells out within two months, exceeding 2026 China projections ([La Repubblica])
• Railway systems face infrastructure damage from extreme heat affecting transport networks ([La Repubblica])
• No TAV camping ban enforced at Susa and Bussoleno with increased security controls ([La Repubblica])
• Italy-Ukraine-Russia war updates continue with latest developments ([La Repubblica])
• FIFA proposes opening organization to private investors under new governance plan ([Le Monde])
• Archibald Prize 2026 people's choice award goes to portrait of Jewish leader after Bondi terror attack ([Guardian World])
• The Weeknd mourns death of musical pioneer who inspired his career ([Vice News])
• Therapist identifies five subtle signs your partner lacks respect ([Vice News])
• Three essential punk albums celebrating 20th anniversary this year ([Vice News])
• Zelda Ocarina of Time remake release date receives update from Nintendo ([Vice News])
• New Fortnite sprites and skins revealed for Chapter 7 Season 4 update ([Vice News])
• Fortnite Chapter 7 Season 4 skins leak ahead of July 30 update ([Vice News])
• DJI Osmo Pocket 4P review highlights benefits of dual-lens system ([The Verge])

Business and economy
• Study protocol published for multimodal prehabilitation program in older adults with chronic limb-threatening ischemia ([PLOS One])
• Research on grant writing coaching demonstrates impact on proposal success rates ([bioRxiv])
• Trump administration orders luxury vehicle fleet for government use amid public criticism ([Guardian World])
• Proposed legislation seeks to defund bike lanes citing DEI initiatives ([Guardian World])
• Amazon's short story collections highlighted as compelling Kindle feature ([The Verge])
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
