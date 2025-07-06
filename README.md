# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-06 11:18 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
July 6, 2025

**Armed conflicts and attacks**
• The inquest into the shooting death of Aboriginal teenager Kumanjayi Walker during a bungled arrest in Australia's Northern Territory is set to deliver its findings, nearly five years after the incident ([Guardian](https://www.theguardian.com/australia-news/2025/jul/06/kumanjayi-walker-family-coroner-final-report-yuendumu-northern-territory))  
• Devastating floods in Texas have killed at least 50 people, including 15 children, with dozens still missing, particularly girls from a Christian summer camp ([Guardian](https://www.theguardian.com/us-news/live/2025/jul/05/texas-flooding-latest-news-updates-guadalupe-river-flood-camp-mystic))  
• Kosovo's parliament failed to elect a new speaker after a bomb threat forced evacuation, continuing political instability ([Bloomberg](https://www.bloomberg.com/news/articles/2025-07-06/kosovo-fails-again-to-elect-speaker-after-bomb-threat-koha-net))  
• A woman was seriously injured after being attacked by an animal while watching zookeepers at work in Queensland, Australia ([Guardian](https://www.theguardian.com/australia-news/2025/jul/06/queensland-zoo-employee-suffers-significant-arm-injury-after-being-mauled-by-animal))  
• Russia launched a large-scale drone and missile attack on Ukraine, prompting condemnation from the UN Secretary-General over risks to nuclear safety ([UN News](https://news.un.org/feed/view/en/story/2025/07/1165336))  
• Liverpool football players attended the funeral in Portugal for Diogo Jota, who died along with his brother in a car crash ([Guardian](https://www.theguardian.com/football/2025/jul/05/liverpool-players-and-citys-ruben-dias-in-portugal-for-diogo-jotas-funeral))

**Disasters and accidents**
• The death toll from Texas flooding rises to at least 50, with 15 children among the victims and a continued search for missing girls from Camp Mystic ([Guardian](https://www.theguardian.com/us-news/live/2025/jul/05/texas-flooding-latest-news-updates-guadalupe-river-flood-camp-mystic))

**Politics and elections**
• US trade partners scramble to finalize deals or secure delays as President Trump prepares to announce new tariff rates, impacting global trade ([Bloomberg](https://www.bloomberg.com/news/articles/2025-07-06/us-trade-partners-race-for-deals-as-trump-readies-tariff-notices))  
• British Foreign Secretary David Lammy announces the UK's re-establishment of diplomatic relations with Syria after years of civil war ([Guardian](https://www.theguardian.com/world/2025/jul/05/britain-re-establishing-diplomatic-relations-with-syria-announces-david-lammy))  
• A Canadian mother who supported Trump's immigration policies was detained by ICE, causing her family to reconsider their political stance ([Guardian](https://www.theguardian.com/us-news/2025/jul/06/trump-voting-family-canadian-mother-detained-immigration-status))

**International relations**
• Brazil hosts the BRICS summit, focusing on global issues like Israel's conflict with Iran and trade tensions with the US under Trump's administration ([ABC News](https://abcnews.go.com/International/wireStory/brazil-hosts-brics-summit-eager-avoid-provoking-trumps-123511526))  
• UN officials highlight the positive role of cooperatives in promoting peace and economic stability in South Sudan ([UN News](https://news.un.org/feed/view/en/story/2025/07/1165256))  
• Iran attempted to recruit Israeli citizens as spies through social media and messaging apps, according to Israeli security services ([Guardian](https://www.theguardian.com/world/2025/jul/06/how-iran-sought-to-recruit-spies-in-israel))

**Business and economy**
• Nationwide Building Society faces backlash for refusing to allow members a binding vote on a 43% pay raise for CEO Debbie Crosbie ([Guardian](https://www.theguardian.com/business/2025/jul/06/anger-as-nationwide-refuses-members-a-binding-vote-on-bosss-43-pay-hike))  
• The Legoland owner's CEO argues that theme parks offer valuable real-life experiences that can compete with digital entertainment, emphasizing the importance of human connection ([Guardian](https://www.theguardian.com/travel/2025/jul/05/were-an-antidote-boss-of-legoland-owner-on-the-thrill-of-theme-parks-in-a-world-of-technology))
Exit code: 0
Report generated at: Sun Jul  6 11:18:24 UTC 2025
```

### 📥 Download
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
