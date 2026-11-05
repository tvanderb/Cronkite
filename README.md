# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 5, 2026](reports/2026-11-05.md)**

*Last updated: 2026-11-05 18:41 UTC · Generated daily at 6:05 AM EST*

```
**November 5, 2026**

**Armed conflicts and attacks**
• Bomb threats disrupt at least 25 commercial flights across Europe, forcing diversions and emergency landings in France, Italy, and other countries; authorities investigate coordinated "hybrid warfare" tactic ([Guardian](https://www.theguardian.com/world/2026/nov/05/bomb-threats-disrupt-flights-across-europe-and-renew-hybrid-warfare-fears), [Guardian Live](https://www.theguardian.com/world/live/2026/nov/05/aer-lingus-plane-bomb-threat-europe-latest-news-updates), [La Repubblica](https://www.repubblica.it/cronaca/2026/11/05/news/allarme_bomba_voli_europa_dublino_fiumicino_helsinki_francia_bulgaria_bruxelles-425700935), [La Repubblica](https://www.repubblica.it/esteri/2026/11/05/news/allarme_bomba_volo_dublino_roma_atterraggio_emergenza_francia-425700771))
• U.S. midterm election results widely viewed as a "thumping rebuke" of the U.S.-Israel relationship as Democrats flip House seats amid voter anger over Gaza policy ([Guardian](https://www.theguardian.com/us-news/2026/nov/04/israel-relationship-midterm-elections))
• Israeli President Isaac Herzog meets rival party leaders as decision nears on forming a government; former military chief Gadi Eisenkot emerges as leading candidate to replace Prime Minister Netanyahu ([Guardian](https://www.theguardian.com/world/2026/nov/05/herzog-netanyahu-eisenkot-israel-election-decision), [Le Monde](https://www.lemonde.fr/international/article/2026/11/05/israel-gadi-eisenkot-l-ancien-chef-d-etat-major-israelien-en-mission-pour-remplacer-benyamin-netanyahou_6807323_3210.html))
• Yemen's President Rashad al-Alimi sacks ministers and military officers in bid to reverse losses against Houthi rebels ([Guardian](https://www.theguardian.com/world/2026/nov/05/yemen-president-sacks-ministers-and-officers-houthis))
• UK found to be "dangerously reliant" on China for critical minerals essential to defense, AI, and renewable energy, per parliamentary report ([Guardian](https://www.theguardian.com/world/2026/nov/05/uk-dangerously-reliant-on-china-critical-minerals-military-ai-renewable-energy))
• Western Sahara: Diplomatic failure risks empowering hardline Polisario Front faction favoring military escalation with Morocco, analysts warn ([Le Monde](https://www.lemonde.fr/afrique/article/2026/11/05/sahara-occidental-l-echec-de-la-diplomatie-risque-de-renforcer-la-frange-du-front-polisario-favorable-a-l-escalade-militaire-avec-le-maroc_6807189_3212.html))
• Melania Trump calls for "durable" ceasefire in Ukraine from White House as war enters another winter ([Le Monde](https://www.lemonde.fr/international/live/2026/11/05/en-direct-guerre-en-ukraine-depuis-la-maison-blanche-melania-trump-appelle-a-un-cessez-le-feu-durable-en-ukraine_6803934_3210.html))
• Email bomb threat campaigns designed to overwhelm and degrade European defense systems, security experts say ([La Repubblica](https://www.repubblica.it/cronaca/2026/11/05/news/strategia_allarme_bomba_email_caos_disfesa-425701240))

**Politics and elections**
• Democrats flip four additional U.S. House seats as Republicans trade blame for "brutal" midterm losses; Nasdaq posts worst day in 18 months amid political uncertainty ([Guardian Live](https://www.theguardian.com/us-news/live/2026/nov/05/midterm-elections-live-latest-updates-mississippi-senate-race), [Guardian](https://www.theguardian.com/business/2026/nov/05/nasdaq-heading-for-worst-day-in-18-months-as-wall-street-sustains-widespread-losses), [La Repubblica](https://www.repubblica.it/esteri/2026/11/05/diretta/elezioni_midterm_usa_2026_risultati
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
