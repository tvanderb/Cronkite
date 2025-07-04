# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-04 11:19 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
Legible News - July 4, 2025 Edition

Armed conflicts and attacks
• The House of Representatives passed Donald Trump's sweeping tax and spending bill by 218 to 214 votes, slashing Medicaid and food stamps while Israel escalated its offensive in Gaza ([Guardian](https://www.theguardian.com/us-news/2025/jul/04/first-thing-corrupt-kleptocracy-democrats-furious-over-passage-of-trump-bill), [Bloomberg](https://www.bloomberg.com/news/articles/2025-07-03/trump-wins-economic-policy-shift-as-house-passes-one-big-beautiful-tax-bill))  
• Hamas leaders are close to accepting a proposed deal for a ceasefire in Gaza but want stronger guarantees of a permanent end to war, while Israel continues its bombardment ([Guardian](https://www.theguardian.com/world/2025/jul/04/gaza-ceasefire-talks-hamas-deal-israel), [Guardian](https://www.theguardian.com/world/live/2025/jul/04/hamas-considers-us-ceasefire-plan-for-gaza-middle-east-live))  
• Russia launched hundreds of drones at Kyiv, injuring at least 23 people, as Trump expressed disappointment over his call with Putin ([Guardian](https://www.theguardian.com/world/live/2025/jul/04/europe-live-latest-news-russia-ukraine-war-putin-zelenskyy))  
• Two female tourists from the UK and New Zealand were killed by an elephant while on a walking safari in Zambia ([Guardian](https://www.theguardian.com/world/2025/jul/03/two-tourists-uk-and-new-zealand-killed-by-elephant-zambia))

Disasters and accidents
• Liverpool footballer Diogo Jota and his younger brother died in a car crash, with mourners gathering in Portugal for their wake ([Guardian](https://www.theguardian.com/football/2025/jul/04/diogo-jota-portugal-liverpool-wake-tributes))

Politics and elections
• Victoria's First Peoples' Assembly will be made permanent and granted decision-making powers as part of a treaty bill ([Guardian](https://www.theguardian.com/australia-news/2025/jul/04/victoria-will-legislate-for-permanent-first-peoples-assembly-later-this-year))  
• Republicans in Congress passed a $3.4 trillion fiscal package that cuts taxes and curtails spending on safety-net programs ([Bloomberg](https://www.bloomberg.com/news/articles/2025-07-03/trump-wins-economic-policy-shift-as-house-passes-one-big-beautiful-tax-bill))  
• The Taliban praised Russia's decision to recognize their rule in Afghanistan ([Guardian](https://www.theguardian.com/world/2025/jul/03/taliban-praise-russias-brave-decision-to-recognise-their-rule-in-afghanistan))  
• The UK's leading AI institute is facing an overhaul with a new focus on defense and national security ([Guardian](https://www.theguardian.com/technology/2025/jul/04/minister-demands-overhaul-of-uks-leading-ai-institute-alan-turing))

Law and crime
• Football agent Jonathan Barnett is being sued in an American court over allegations of human trafficking, torture, and rape ([Guardian](https://www.theguardian.com/football/2025/jul/04/jonathan-barnett-football-agent-accused-of-trafficking-torture-rape))  
• Italian oil firm Eni is accused of trying to silence green activists through defamation suits ([Guardian](https://www.theguardian.com/environment/2025/jul/04/italian-oil-firm-eni-accused-of-trying-to-silence-green-activists))  
• A Croatian court sentenced a gunman to 50 years in prison for a nursing home shooting that killed six people, including his own mother ([ABC News](https://abcnews.go.com/International/wireStory/croatian-court-sentences-gunman-50-years-nursing-home-123444186))

International relations
• A landmark US study finds troubling levels of PFAS near wastewater plants and sludge sites in 19 states, raising questions about waste management ([Guardian](https://www.theguardian.com/us-news/2025/jul/04/pfas-pollution-sewage-wastewater))  
• Rodolphe Saadé, a billionaire, plans to acquire the French media company Brut through the media subsidiary of CMA CGM ([Le Monde](https://www.lemonde.fr/economie/article/2025/07/04/rodolphe-saade-veut-acquerir-brut-via-la-filiale-medias-de-cma-cgm_6618116_3234.html))  
• Chile and Argentina are experiencing unprecedented cold temperatures, with some areas recording -15°C (5°F) ([UN News](https://news.un.org/feed/view/en/story/2025/07/1165286))  
• Young farmers worldwide are struggling to inherit agricultural land as older generations hold onto it tightly ([UN News](https://news.un.org/feed/view/en/story/2025/07/1165316))
Exit code: 0
Report generated at: Fri Jul  4 11:19:34 UTC 2025
```

### 📥 Download
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
