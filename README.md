# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[May 25, 2026](reports/2026-05-25.md)**

*Last updated: 2026-05-25 14:16 UTC · Generated daily at 6:05 AM EST*

```
- **Armed conflicts and attacks**
  • Researchers discovered a surprisingly effective way to accelerate human bonding, with surprising results not tied to shared interests. (Vice News)
  • Iran denies deal with the US is imminent despite some progress in negotiations. (The Guardian World)
  • Trump Tower in Georgia will be built on land partially owned by a son of a US sanctions-hit leader. (Guardian World)
  • Presidentielle 2027: For Bruno Retailleau, an adventure almost on the heels of François Fillon. (Le Monde)
  • The ‘chalance’ dating trend is going viral for criticizing modern romance’s lack of effort. (Vice News)
  • A rare Rubens notebook sheet goes on display in the city of Antwerp. (Guardian World)
  • Oil prices drop below $100 a barrel, sparking hopes for a new Iran peace deal. (Guardian World)
  • US and Iran inch closer to a peace deal as Trump faces criticism from GOP hawks. (Guardian World)
  • Rare Rubens notebook sheet goes on display in the artist’s home city of Antwerp. (Guardian World)
  • Afghanistan activists report sexual assault and beatings in Israeli detention. (The Guardian)
  • The Mandalorian and Grogu feature in Disney’s latest Star Wars film with lowest opening ever. (Guardian World)
  • Roland-Garros 2026 sees Wawrinka, Elina Svitolina, and several others in a tight bracket. (Le Monde)
  • The ‘affaire Patrick Bruel’ at the Paleo Festival in Nyon calls out inadmissible behavior. (Le Monde)
  • Hichem Aboud faces new charges after a 2019 incident involving a public event. (Le Monde)

- **Disasters and accidents**
  • Chemical tank crack increases fears after a major explosion in California. (Guardian World)
  • Flash floods hit New York and a heat dome grips Europe in a record series. (The Guardian World)
  • Australian flotilla activists arrive home alleging sexual assault and beatings in Israeli detention. (The Guardian)
  • A psychologist reveals a blunt theory behind the growing male loneliness epidemic. (Vice News)
  • Australian actor Grizz Chappy dies at age 52. (Guardian World)
  • Human rights crisis in the US sees transgender Americans forced to flee persecution. (Spiegel)
  • A suicide bombing near a railway track in Pakistan kills at least 23 people. (Guardian World)

- **Politics and elections**
  • Labour needs a 'system reset' to tackle youth unemployment and will deliver a report to the coalition. (The Guardian World)
  • Australian flotilla activists accuse their leader of stripping and beating them. (The Guardian)
  • The 4 phrases that can quietly destroy a relationship over time, according to an expert. (Vice News)
  • A rare Rubens notebook sheet goes on display in his hometown of Antwerp. (Guardian World)

- **Law and crime**
  • Law enforcement in Cambodia welcomes Australian flotilla activists after sexual assault allegations. (Le Monde)
  • US and Iran inch closer to a peace deal as Trump faces criticism from GOP hawks. (Guardian World)
  • A man accused of a 2019 incident denies wrongdoing in a major court case. (Le Monde)
  • Indonesian court sentences two men in a high-profile kidnapping case. (The Guardian World)
  • "Chalance" dating trend goes viral for criticizing modern romance. (Vice News)
  • Australian actor Grizz Chappy dies after multiple roles. (The Guardian)
  • A rare Rubens notebook sheet goes on display in the city of Antwerp. (Guardian World)

- **Armed conflicts and attacks**
  • NATO and Russia escalate dialogue ahead of potential talks on Ukraine. (Le Monde)
  • The ‘chalance’ trend is sparking debate about the future of modern romance. (Vice News)
  • A US businessman defends himself in a high-profile defamation case. (The Guardian World)
  • Iran denies deal with US is imminent despite some progress. (The Guardian World)

- **International relations**
  • The BHP defies its own climate strategy by investing in high-polluting diesel trucks. (The Guardian World)
  • Russia calls on foreign nationals to leave Kyiv ahead of new airstrikes. (Le Monde)
  • Argentina faces internal conflict following a presidential election. (Le Monde)
  • Ukraine calls for peace as Russia intensifies strikes. (The Guardian)
  • Oil prices fall to a two-week low amid fears of a new Iran deal. (Guardian World)
  • Rare Rubens notebook sheet goes on display in Antwerp. (Guardian World)
  • A major tycoon files leaked documents opposing climate action. (The Guardian)
  • Human rights crisis in DRC with suspected Ebola cases raising alarm. (Guardian World)
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
