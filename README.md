# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[July 11, 2026](reports/2026-07-11.md)**

*Last updated: 2026-07-11 11:59 UTC · Generated daily at 6:05 AM EST*

```
July 11, 2026

**Armed conflicts and attacks**
• Senators reach agreement with Donald Trump on Russia sanctions bill (Bloomberg)
• UN Security Council warns of lost continuity on Iran's nuclear program following US-Israel strikes (United Nations News)
• Ukraine reports downing of 111 drones and two Russian missiles overnight; ten injured in Kiev (Le Monde)
• Wildfire in southern Spain kills at least 12 in Los Gallardos, Almeria province (Guardian World)
• Protests erupt across Indian West Bengal state after rape and murder of 11-year-old girl (Guardian World)
• Pianist Jayson Gillham expresses disappointment after losing discrimination case against Melbourne Symphony Orchestra (Guardian World)

**Disasters and accidents**
• Venezuela earthquake death toll exceeds 4,000 as scale of recovery effort becomes clear (Guardian World)

**Politics and elections**
• France's new moon in Cancer has astrologers predicting impacts for zodiac signs (Vice News)
• Spain defeats Belgium 2-1 in World Cup 2026 group stage with tactical coaching from Luis de la Fuente (Le Monde)
• Marine Le Pen's popularity remains unaffected despite upheld conviction (Guardian World)
• France-Australia rugby match features tactical coaching duo of Ntamack-Jalibert versus Galthié's team (Le Mode)
• Heatwave in France reaches 39°C; 24 departments on red alert as third heat wave hits in two months (Le Monde)
• Canadian-US bridge deal includes profit-sharing arrangement to secure Trump approval for Gordie Howe International Bridge (Bloomberg)

**Law and crime**
• Man killed by ICE agents in Texas never "weaponized" his vehicle, witnesses say (Guardian World)
• Investigation into Ann Widdecombe's murder releases man arrested on suspicion (Guardian World)
• Child abuse survivor identifies orphans housed at Christian Brothers properties where abuse occurred (Guardian World)
• French mayor and commercial contractor defrauded communities of €38,000 in suspicious business practices (Le Mode)
• Mexican man killed by ICE in Houston reignites debate on immigration policing amid accelerating deportations (Le Monde)
• Patrick Bruel investigated in new rape complaint (Le Monde)

**International relations**
• Europe considering proposals for navigational fees in Strait of Hormuz (Guardian World)
• Datacenters drive big tech carbon emissions to one-third of France's total (Guardian World)
• Scientists discover world's fastest spider capable of outrunning average human jogger (Vice News)
• Alfred Dreyfus statue to receive permanent home in central Paris (Guardian World)
• BBC presenter Dermot Murnaghan dies after battling prostate cancer (Guardian World)
• France-Iran tensions escalate as Mojtaba Khamenei vows revenge for father's death amid new Oman negotiations (La Repubblica)
• Russia-Ukraine conflict: Kiev reports significant drone and missile losses overnight (Le Monde)

**Business and economy**
• NHS anaesthetist shortage prevents 1.5 million operations annually, report finds (Guardian World)
• Major datacenters push big tech carbon emissions to one-third of France's total (Guardian World)
• SK Hynix debuts as Nvidia's key RAM supplier with trillion-dollar valuation (The Verge)
• FCC cracks down on DJI front companies attempting to circumvent foreign drone ban (The Verge)
• Lottery winner shares experience of spending $160,000 on fun and future investments (Business Insider)
• BBC presenter Dermot Murnaghan dies following prostate cancer diagnosis (Guardian World)
• Research examines socioeconomic factors affecting early breastfeeding initiation in Bangladesh (PLOS One)

**Technology**
• Meta discontinues Muse Image AI feature citing privacy concerns with users (Guardian World)
• Scientists develop new asteroid deflection method involving space drills (Vice News)

**Health and science**
• Research reveals dynamic positioning of RPC34 winged helix in RNA polymerase III elongation complex (PNAS)
• Study shows meiotic cohesin Rec8 imposes fitness costs on fission yeast gametes (PNAS)
• Research explores how information and emotion influence behavioral choice through user credibility (PLOS One)

**Environment**
• London Underground temperatures exceed legal limits for cattle during heatwave (Guardian World)
• Lake Chad remains Africa's most important wetland for waterbirds despite ongoing conflicts (PNAS)

**Culture and entertainment**
• Ryanair eliminates family seating policy but children's fees continue to accumulate (Guardian World)
• EA removes College Football 27 microtransactions following player boycott (Vice News)
• Music industry proposes AI-generated music label amid platform surge (Le Monde)
• Erling Haaland celebrated as "little boy who grew into huge Viking" by hometown fans (Guardian World)
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
