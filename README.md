# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-14 11:20 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
### Legible News - July 14, 2025

**Armed conflicts and attacks**
• Israel's military actions in Gaza continue to draw international attention. Recent reports indicate that at least 10 people, including six children, were killed in an airstrike while waiting for water near a distribution site, raising the death toll to over 50 in the past few days ([Guardian](https://www.theguardian.com/world/2025/jul/13/dozens-of-palestinians-killed-in-latest-israeli-attacks-near-food-aid-distribution-sites-medics-and-witnesses-say)).  
• Ukrainian President Volodymyr Zelenskyy has expressed disappointment over the lack of serious peace negotiations with Russia, emphasizing that Ukraine should prepare for a future without a ceasefire ([Guardian](https://www.theguardian.com/world/2025/jul/13/dose-of-realism-would-allow-kyiv-to-focus-on-halting-russian-advance-ukraine)).  
• US President Donald Trump has announced plans to expedite the sale of Patriot air defense systems and other weapons to Ukraine, amid growing tensions with Russia ([Guardian](https://www.theguardian.com/us-news/2025/jul/14/trump-ukraine-weapons-patriot-russia)).

**Disasters and accidents**  
• A Beechcraft B200 aircraft crashed at London Southend Airport, resulting in an ongoing investigation. The airport remains closed, and casualty figures are yet to be confirmed ([Guardian](https://www.theguardian.com/uk-news/2025/jul/14/southend-plane-crash-essex-casualties-investigation)).  
• Families of the victims of the recent Air India crash are seeking further clarity and transparency from investigators after the initial report was deemed vague. The report suggested the plane's fuel switches were cut off, but questions remain unanswered ([Guardian](https://www.theguardian.com/world/2025/jul/13/air-india-crash-victims-families-not-satisfied-with-vague-initial-report)).

**Politics and elections**  
• The EU is responding to the US President's threat of imposing 30% tariffs on the bloc's imports. EU ministers have convened urgent talks to address the potential economic impact ([Guardian](https://www.theguardian.com/world/live/2025/jul/14/europe-ukraine-russia-donald-trump-tariff-latest-live-news-updates)).  
• The New South Wales Liberal party will challenge the narrow defeat in the Sydney seat of Bradfield, where independent candidate Nicolette Boele won by a margin of 26 votes after a recount ([Guardian](https://www.theguardian.com/australia-news/2025/jul/14/nsw-liberals-court-challenge-sydney-seat-bradfield-nicolette-boele-gisele-kapterian)).

**International relations**  
• The Bank of Japan is expected to revise at least one of its inflation forecasts upward due to higher-than-expected rice and food prices, ahead of their policy meeting later this month ([Bloomberg](https://www.bloomberg.com/news/articles/2025/07/14/boj-is-said-likely-to-consider-raising-inflation-forecast)).  
• The UN will host a high-level forum to accelerate action on the Sustainable Development Goals (SDGs) as the 2030 target approaches. The forum will focus on health, gender equality, and oceans ([UN News](https://news.un.org/feed/view/en/story/2025/07/1165381)).

**Business and economy**  
• The Bank of Japan has completed the sale of stocks purchased from banks during the 2000s domestic banking crisis and the Lehman Shock, turning market focus to its larger exchange-traded funds (ETFs) portfolio ([Bloomberg](https://www.bloomberg.com/news/articles/2025/07/14/boj-finishes-offloading-bank-stocks-bringing-attention-to-etfs)).
Exit code: 0
Report generated at: Mon Jul 14 11:19:49 UTC 2025
```

### 📥 Download
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-14` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-13` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-12` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-11` artifact
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
