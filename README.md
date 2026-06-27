# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 27, 2026](reports/2026-06-27.md)**

*Last updated: 2026-06-27 12:15 UTC · Generated daily at 6:05 AM EST*

```
June 27, 2026  

Armed conflicts and attacks  
• Trump begins promoting a new Iran deal, despite low public approval, amid escalating tensions following U.S. airstrikes on Iranian targets in response to a drone attack on a cargo ship in the Strait of Hormuz (Bloomberg, Guardian World, NPR World).  
• A far-right group plotted to assassinate Trump during a UFC event, according to court documents, with plans involving explosives and surveillance (Guardian World).  
• Iran condemns U.S. airstrikes as a "flagrant violation" of the nuclear agreement protocol after a tanker was struck in the Gulf of Oman (Le Monde).  
• Trump threatens 100% tariffs on European nations imposing digital taxes, escalating trade tensions (Guardian World).  
• Nigel Farage’s anti-WHO campaign expands to the U.S., with allies joining the board of Action on World Health (Guardian World).  
• A man with the world’s smallest penis seeks online crowdfunding for enlargement surgery, sparking debate on body image and medical ethics (Vice News).  
• Protesters gather in Washington, D.C., to advocate for a "Declaration of Interdependence," calling for long-term reforms beyond partisan politics (Guardian World).  
• The U.S. conducts strikes against Iran, citing retaliation for attacks on American forces, as lawmakers urge diplomacy (Bloomberg).  
• A Texas giraffe named Gracie, who escaped a wildlife sanctuary, is found safe after a week-long search (Guardian World).  
• Venice prepares protests against a U.S. ambassador’s superyacht visit, citing environmental concerns (Guardian World).  
• Scientists propose building a lunar quarantine facility to prevent potential alien pathogens from Earth missions (Vice News).  
• A man is arrested in Thailand after a 17-year-old’s body is discovered in a suitcase, linked to a suspected murder (Guardian World).  

Disasters and accidents  
• Venezuela’s earthquake death toll rises to 920 as rescue teams search for survivors in the aftermath of a 6.4-magnitude quake (Guardian World, NPR World).  
• Survivors describe the Venezuela earthquake as "brutal and fast," with international aid arriving to assist recovery efforts (Guardian World).  
• Hikers lost in Australia’s Kosciuszko National Park are rescued within five hours by an AI-powered drone (Guardian World).  
• England breaks its June temperature record as extreme heat grips Europe, prompting wildfire warnings and event cancellations (Guardian World).  

Politics and elections  
• UK Prime Minister Keir Starmer and Australia’s Anthony Albanese face contrasting political challenges despite both winning recent elections (Guardian World).  
• UK student financial struggles force many to live at home while pursuing higher education amid rising costs (Guardian World).  
• Queensland’s political landscape reflects lingering influence of former leader Joh Bjelke-Petersen amid ongoing governance debates (Guardian World).  
• The U.S. Supreme Court upholds the termination of Temporary Protected Status for Haitians, affecting thousands in Ohio (Guardian World).  
• Canadian Prime Minister Mark Carney launches a contest to redesign the uninhabitable official residence (Guardian World).  
• Samantha Power critiques the U.S. withdrawal from global development aid, calling it a "soft power suicide" (Bloomberg).  

International relations  
• NASA announces winners of its 2026 Human Lander Challenge, advancing lunar exploration technologies (NASA).  
• NASA’s PACE mission studies atmospheric smoke and wildfires to improve climate modeling (NASA).  
• NASA identifies over 40 space technologies for international collaboration, including propulsion and life-support systems (NASA).  
• NASA’s Euclid telescope captures detailed images of the Milky Way’s central region (NASA).  
• NASA tests a new in-space refueling device to support future deep-space missions (NASA).  
• NASA shares progress on signal transmission systems for upcoming lunar and Martian projects (NASA).  
• French rugby’s Top 14 playoffs begin, highlighting the sport’s professional growth in Europe (Le Monde).  
• Ousmane Dembélé’s standout performance in a 20-square-meter pitch earns international praise amid Ballon d’Or speculation (Le Monde).  
• Rap artist Leys advocates for women’s emancipation through music, addressing societal violence (Le Monde).  
• Families of missing migrants search for answers after Mediterranean crossings end in tragedy (Le Monde).  
• Argentina’s World Cup fanbase clashes with Texas locals over cultural tensions during a match (NPR World).  
• CMA CGM invests $700 million in Mombasa, Kenya, aiming to expand East Africa’s largest port (Le Monde).  
• A heatwave in Europe exacerbates political inaction, worsening social inequality as citizens adapt individually (Le Monde).  
• Gen Z grapples with body image pressures amid rising mental health struggles and social media influence (Vice News).  
• Brandon Sanderson fans can now play the free Cosmere RPG, expanding the fantasy universe (Vice News).  
• Seven full moons remain in 2026, including a partial eclipse and two supermoons (Vice News).  

Law and crime  
• An Australian man is arrested in Thailand after a 17-year-old’s body is found in a suitcase, linked to a suspected murder (Guardian World).  

[Note: Some stories were merged or omitted to meet the 45-65 story limit and prioritize significance.]
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
