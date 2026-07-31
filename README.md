# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[July 31, 2026](reports/2026-07-31.md)**

*Last updated: 2026-07-31 13:02 UTC · Generated daily at 6:05 AM EST*

```
July 31, 2026

**Armed conflicts and attacks**
• US airstrikes hit multiple Iranian targets overnight amid escalating tensions following earlier attacks on Iran (The Guardian World, NPR World)
• Trump announces "historical agreement" for Hamas to disarm, though details remain unclear and significant obstacles persist (Le Monde, NPR World)
• Iran responds to US strikes by targeting Israeli assets and seeking to regain control over conflict dynamics (Le Monde)
• Saudi Arabia prepares major sea and potential land offensive against Houthis in Yemen (The Guardian World)
• Ukraine conflict continues with Russian reports of strikes on Loukoël refinery in Volgograd region (Le Monde)
• At least 34 people killed as thousands cross from Morocco to Spanish enclave of Ceuta (The Guardian World)
• Wildfire near Sizewell nuclear plant causes "total devastation" to Suffolk landscape (The Guardian World)
• Ebola outbreak in Democratic Republic of Congo becomes fastest growing in virus history (The Guardian World)

**Disasters and accidents**
• Climate crisis intensifying wildfire conditions across Europe, described as "extremely scary findings" (The Guardian World)
• British-Azerbaijani man arrested in Cyprus for allegedly spying on UK airbase for Iran (The Guardian World)
• Hull funeral director Robert Bush sentenced to 20 years for leaving bodies to rot in mortuary (The Guardian World)
• Man walks 10 miles down mountain after being impaled by trekking pole (Vice News)
• British man seeks court permission to attend son's funeral after fall from hotel window in Cyprus (ABC News)

**Politics and elections**
• Trump scheduled to meet cabinet at Camp David as Iran conflict continues (The Guardian World)
• Top Democrats accuse Republicans of becoming "gelatinous blobs" on Iran war strategy (The Guardian World)
• Fifa planning to pursue private investment despite controversy, with Gianni Infantino supporter resigning in protest (Le Monde)
• Turkey's Erdogan faces mounting pressure as opposition gains ground in key regions (The Guardian World)
• UK petrol prices reach Iran war highs, adding strain to households (The Guardian World)
• BP puts North Sea oil and gas business up for sale (The Guardian World, Bloomberg)

**Law and crime**
• Spain's Sánchez blames trafficking gangs as estimated 60,000 migrants reach Ceuta (The Guardian World, Le Monde)
• ICAC hears evidence of friendship breakdown between Reformers members in Australian corruption inquiry (The Guardian World)
• "Rob has the bucks cash": NSW Liberals used Reformers funds for personal expenditure, ICAC hears (The Guardian World)
• Archbishop of Canterbury supports £100m pledge to help communities affected by historic enslavement (The Guardian World)

**International relations**
• EU to require AI labels on authentic-looking content (The Guardian World)
• UN Secretary-General race sees Rebeca Grynspan emerge as frontrunner (Le Monde)
• France seizes assets of pro-Putin propagandist Xenia Fedorova under expulsion order (Le Monde)
• DRC announces negotiated surrender of FDLR rebels in eastern region, complicating Rwanda peace process (Le Monde)
• US government map of Africa mislabels every country at global conference (The Guardian World)
• France seizes assets of pro-Putin propagandist Xenia Fedorova under expulsion order (Le Monde)
• India student protesters use Instagram memes to counter Modi's WhatsApp/X strategy (Bloomberg)
• Turkey's Erdogan faces mounting pressure as opposition gains ground in key regions (The Guardian World)

**Business and economy**
• BP puts North Sea oil and gas business up for sale (The Guardian World)
• Samsung Galaxy Watch 9 available at $40 discount at Costco with over $50 in freebies (The Verge)
• "It ain't the same": bitter battle to free Ben & Jerry's unfolds (The Guardian World)
• Tesla considering sale of Chinese operations as SpaceX merger discussions continue (La Repubblica)
• Archbishop of Canterbury supports £100m pledge to help communities affected by historic enslavement (The Guardian World)

**Technology**
• Sony responds to PlayStation player backlash over PS5 physical disc elimination (Vice News)
• AI labels to be compulsory on authentic-looking content under EU rules (The Guardian World)

**Science and health**
• New research shows repeated sampling outperforms self-refinement techniques at equal token cost in AI models (arXiv)
• Predicting microscopic axon topology in cortical neurospheres through interactive tracking pipeline (bioRxiv)

**Culture and entertainment**
• Sony responds to PlayStation player backlash over PS5 physical disc elimination (Vice News)
• Call of Duty Black Ops 1 PS5 update fixes sniper issues and party matchmaking (Vice News)
• Fortnite Ironmouse sprite release date confirmed after vaulting (Vice News)
• 4 underrated mid-90s songs that accidentally created 2000s nu-metal identified (Vice News)
• What people want to inherit from dead relatives versus what they don't (Vice News)

**Weather and environment**
• Climate crisis supercharging Europe's wildfire weather patterns (The Guardian World)
• Huge great white shark spotted traveling up US and Canada coasts as sightings surge (The Guardian World)
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
