# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-10 11:19 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
July 10, 2025

Armed conflicts and attacks
• Ukraine has arrested a Chinese father and son on suspicion of spying on the Neptune missile program, a critical defense against Russia. ([Source])
• UNAIDS reports that high-risk HIV groups, including LGBTQ+ individuals, face record levels of criminalization, threatening decades of progress in the fight against AIDS. ([Source])
• The Trump administration has imposed sanctions on Francesca Albanese, the UN official investigating human rights abuses in Palestinian territories. ([Source])
• A deadly flash flood in central Texas over the July Fourth weekend claimed over 100 lives, highlighting the challenges of ensuring early warnings reach vulnerable populations. ([Source])
• Houthi forces attacked a cargo ship in the Red Sea, killing four and leaving 14 missing. Seven crew members were rescued. ([Source])

Politics and elections
• Data shows that 1.7 million children are affected by the UK's two-child benefit cap, an increase of 37,000 in the past year. ([Source])
• Donald Trump announced a 50% tariff on Brazilian products, linking the move to the "witch-hunt" trial against Bolsonaro. ([Source])
• A court in Sydney rejected a developer's bid to turn a boarding house into luxury apartments, citing the importance of affordable housing. ([Source])
• Experts warn that Republican redistricting in Texas could shape the outcome of the next year's elections. ([Source])
• The European Commission President, Ursula von der Leyen, is facing a rare vote of censure in the European Parliament over the EU's rightward drift. ([Source])

Disasters and accidents
• Glaciers in northern Pakistan are melting at an accelerated rate due to record temperatures, causing deadly floods and landslides. ([Source])
• NASA has deployed aircraft to assist in recovery efforts following recent flooding in Texas. ([Source])

International relations
• NASA is using AI to make science data easier to find, addressing the challenge of mismatched terminology in online databases. ([Source])
• A Canadian couple's message in a bottle, thrown into the Atlantic in 2012, was found 13 years later in an Irish bay. ([Source])
• The PSG football team defeated Real Madrid 4-0 to advance to the final of the Club World Cup. ([Source])
• A 19-year-old surfer who went missing off the Australian coast was found on a remote island 14 km away. ([Source])
• French comedian Bun Hay Mean, known for his role in "Astérix & Obélix: L'Empire du Milieu," was found dead at the age of 43. ([Source])
Exit code: 0
Report generated at: Thu Jul 10 11:19:08 UTC 2025
```

### 📥 Download
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-10` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-09` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-08` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-07` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-06` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-05` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-04` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-03` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-03` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-03` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-<YYYY-MM-DD>` artifact

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
