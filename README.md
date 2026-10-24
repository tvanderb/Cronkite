# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 24, 2026](reports/2026-10-24.md)**

*Last updated: 2026-10-24 14:27 UTC · Generated daily at 6:05 AM EST*

```
**Legible News — Daily Report**  
**October 24, 2026**

---

### Armed conflicts and attacks
• Israel razes a neighborhood in Hebron, West Bank, displacing Palestinian families after two Israeli soldiers were killed; the operation described as collective punishment. ([Guardian](https://www.theguardian.com/world/2026/oct/24/israel-soldiers-raze-west-bank-neighbourhood-hebron-families-from-homes), [Guardian](https://www.theguardian.com/world/2026/oct/23/netanyahu-orders-very-extensive-operation-west-bank-two-israeli-soldiers-killed))  
• Ukraine and Russia signal openness to new peace talks; Melania Trump reportedly involved in diplomatic outreach, though major obstacles remain. ([ABC News](https://abcnews.com/International/wireStory/ukraine-russia-eye-new-peace-talks-melania-trumps-137534005))  
• Gunmen open fire at a church funeral in Jordan, killing eight and wounding 40. ([Guardian](https://www.theguardian.com/world/2026/oct/24/seven-killed-and-40-injured-after-gunmen-open-fire-at-church-funeral-in-jordan))  
• Saudi airstrikes hit Houthi-held Sanaa, Yemen, killing at least four people. ([Le Monde](https://www.lemonde.fr/international/article/2026/10/24/au-yemen-des-frappes-saoudiennes-font-au-moins-quatre-morts-a-sanaa-capitale-aux-mains-des-houthistes_6799703_3210.html))  
• Ukrainian drone strike kills three in Russian-occupied Kharkiv oblast. ([Le Monde](https://www.lemonde.fr/international/live/2026/10/24/en-direct-guerre-en-ukraine-trois-personnes-tuees-par-un-drone-ukrainien-dans-la-partie-occupee-de-l-oblast-de-kharkiv_6796922_3210.html))  
• Drinking water supplies dwindle in a Yemeni city besieged by Houthi rebels. ([NPR](https://www.npr.org/2026/10/24/g-s1-149729/drinking-water-supplies-dwindle-in-yemeni-city-besieged-by-houthi-rebels))  
• Marco Rubio urges Cubans to act now for political change, signaling harder U.S. line. ([Guardian](https://www.theguardian.com/us-news/2026/oct/23/marco-rubio-cuba-trump))  
• Australian Greens senator Jordon Steele-John takes leave from parliament after misconduct allegations. ([Guardian](https://www.theguardian.com/australia-news/2026/oct/23/jordan-steele-john-in-limbo-greens-misconduct-allegations-ntwnfb), [Guardian](https://www.theguardian.com/australia-news/2026/oct/24/greens-senator-jordon-steele-john-confirms-leave-from-parliament-ntwnfb))  
• Helen Haines, Australian MP, improving after losing both legs in alleged attack. ([Guardian](https://www.theguardian.com/australia-news/2026/oct/24/helen-hainess-condition-improves-days-after-losing-both-legs-from-alleged-attack-ntwnfb))  
• Typhoon Champi kills one, injures over 500 in Taiwan before heading toward China. ([Guardian](https://www.theguardian.com/world/2026/oct/24/typhoon-champi-kills-one-and-injures-more-than-500-in-taiwan-as-it-heads-to-china))

---

### Disasters and accidents
• Storm Boelo brings 80 mph gusts and heavy rain to northern UK. ([Guardian](https://www.theguardian.com/world/2026/oct/24/storm-boelo-80mph-winds-heavy-rain-northern-uk))  
• British woman dies trying to save her two sons during a snorkeling trip in the Bahamas. ([Guardian](https://www.theguardian.com/world/2026/oct/24/british-woman-dies-trying-to-save-sons-on-bahamas-snorkelling-trip))  
• Thunderstorms, heavy rain, and flash flooding forecast for much of Australia. ([Guardian](https://www.theguardian.com/australia-news/2026/oct/24/thunderstorms-heavy-rain-and-flash-flooding-predicted-for-much-of-australia))  
• Nine years after the Grenfell Tower fire, UK buildings still lag on safety retrofits. ([Le Monde](https://www.lemonde.fr/economie/article/2026/10/24/neuf-ans-apres-l-incendie-dramatique-de-la-tour-grenfell-a-londres-la-tres-lente-mise-aux-normes-des-immeubles-britanniques_6799682_3234.html))  
• In Naples, 20 people hospitalized in two days after accidentally ingesting gasoline amid fuel shortage panic. ([La Repubblica](https://napoli.repubblica.it/cronaca/2026/10/23/news/emergenza_carburante_cardarelli_20_chiamate_benzina_ingerita_accidentalmente-425670435/))  
• Britons stockpile tinned food, toilet paper, and power banks following government preparedness advice. ([Guardian](https://www.theguardian.com/society/2026/oct/24/tinned-food-loo-roll-power-banks-brits-stockpiling-government-advice))

---

### Politics and elections
• Jordan Bardella re-elected president of France’s National Rally with 98.98% of the vote as sole candidate. ([Le Monde](https://www.lemonde.fr/politique/article/2026/10/24/au-congres-du-rn-a-orleans-jordan-bardella-seul-candidat-a-sa-succession-est-reelu-president-du-parti-avec-98-98-des-voix_6799707_823448.html))  
• Trump pushes DOJ lawsuit over Alaska Senate race; tests political
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
