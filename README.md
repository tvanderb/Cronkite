# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 20, 2026](reports/2026-10-20.md)**

*Last updated: 2026-10-20 15:36 UTC · Generated daily at 6:05 AM EST*

```
October 20, 2026

**Armed conflicts and attacks**
• Houthi attack kills 53 in biggest single loss of life since Yemen civil war reignited (Guardian World)
• UK to deploy fighter jets to protect Saudi Arabia from Houthi attacks (Guardian World)
• Israeli police detain 10 people in rare raid against West Bank settlers (Guardian World)
• Serbian prosecutor who investigated Belgrade Trump tower project 'targeted with spyware' (Guardian World)
• French army to deploy military forces during expected weekend protests (Guardian World)
• Italy to deploy 500 troops to Milan after days of protests and looting (Guardian World)
• US bans use of China's DeepSeek AI tools by government agencies (Guardian World)
• Madagascar emerges as new hub for Russian recruitment and influence (Le Monde)
• Slovakian companies become new European hub for weapons production (Le Monde)
• Trump hints at pulling back threat of US bombardier boycott (Bloomberg)
• Hegseth visits Israel, meets Netanyahu with days before vote (Bloomberg)

**Politics and elections**
• Trump continues midterm campaign blitz in North Carolina – US politics live (Guardian World)
• BBC Three and BBC Scotland TV channels to be shut down next year (Guardian World)
• Michigan heckler the son of Republican adviser paid for 'influencer marketing' against El-Sayed (Guardian World)
• Statement by President von der Leyen on Europe's Northern Neighbourhood: A New Strategy for the Arctic (Government EU Newsroom)
• Remarks by Commissioner Šefčović at European Parliament Plenary debate on EU-UK Summit (Government EU Newsroom)
• Midterms show strong turnout despite Trump's fraud allegations (Le Monde)
• Student protests continue but hampered by university closures (Le Monde)

**Business and economy**
• Billionaire Mukesh Ambani launches India's biggest-ever IPO (Guardian World)
• Hackers hit AI coding tool OpenCode, running up charges on users' AI accounts (Industry TechCrunch)
• Antigravity halves drone price by swapping headset for wristwatch control (Industry The Verge)
• Theranos whistleblower barely recognizes Elizabeth Holmes in new documentary (Industry Fortune)
• Rates of diabetic retinopathy regression among patients in Indian Health Service program 2015-2020 (Academic PLOS One)
• Self-reported TB prevalence among rural Indian populations: community-based study (Academic PLOS One)
• UK to deploy fighter jets to protect Saudi Arabia from Houthi attacks (Guardian World)
• French army to deploy military forces during expected weekend protests (Guardian World)
• Italy to deploy 500 troops to Milan after days of protests and looting (Guardian World)

**Law and crime**
• Brendan Nugent facing three charges over alleged attack on MP Helen Haines (Guardian World)
• Kenyan starvation cult leader guilty of murder of 190 children and one adult (Guardian World)
• Prosecutor Rima Hassan's terrorism apology case: prison with suspension sought (Le Monde)
• Helen Haines loses leg as surgeons fight to save other after alleged attack in Wangaratta (Guardian World)

**International relations**
• Vast Beatles museum hailed as 'extraordinary' by Paul McCartney to open in Liverpool in 2028 (Guardian World)
• Giving £2 a day to people in Amazon helps protect rainforest, pilot project finds (Guardian World)
• 'Coral Island' announces major update and Nintendo Switch 2 release (Vice News)
• The bizarre history of professional farters, including a few who got stinking rich as 'Fartists' (Vice News)
• Did people really die in the 'Evil Dead' cabin? Here's what actually happened (Vice News)
• Sex is just as effective as nasal spray for stuffy nose, scientists say (Vice News)
• Most long-term singles are actually happy being single, new study finds (Vice News)
• US grants deportation reprieve to migrants from Ukraine and Sudan (Guardian World)
• Myanmar's ousted leader Aung San Suu Kyi seen in rare photos after receiving gift from King Charles (Guardian World)
• In Lebanon's south, olive harvest occurs under Israeli occupation shadow (Le Monde)
• French army to deploy military forces during expected weekend protests (Guardian World)
• Student protests continue but hampered by university closures (Le Monde)

**Health and medicine**
• Actor Christina Applegate reveals she was misdiagnosed with multiple sclerosis (Guardian World)
• Rates of nonproliferative diabetic retinopathy regression among patients with mild cases in Indian teleophthalmology program 2015-2020 (Academic PLOS One)

**Environment**
• Giving £2 a day to people in Amazon helps protect rainforest, pilot project findings (Guardian World)

**Science and technology**
• Sex is just as effective as nasal spray for stuffy nose, scientists report (Vice News)
• Hackers hit AI coding tool OpenCode, running up charges on users' AI accounts (Industry TechCrunch)
• Antigravity halves drone price by swapping headset for wristwatch control (Industry The Verge)

**Society and culture**
• 'We really need help': RSPCA faces capacity crisis as cats arrive faster than they can be rehomed (Guardian World)
• A young life 'dominated by gambling': Victorian coroner's findings on death of 22-year-old (Guardian World)
• I took my 75-year-old mom on a trip to 3 countries, had to ditch typical travel style (Industry Business Insider)
• We got my older son a phone at 12, and I regretted it. Still got younger son at same age (Industry Business Insider)
• 5 classic horror movies that used real human skeletons instead of props (Vice News)
• The bizarre history of professional farters, including those who got rich as 'Fartists' (Vice News)
• Getting Ziggy with it: David Bowie's alter egos inspire dance show transforming his songs (Guardian World)

**Disasters and accidents**
• Kenyan starvation cult leader guilty of murder of 190 children and one adult (Guardian World)

**Media and entertainment**
• BBC Three and BBC Scotland TV channels to be shut down next year (Guardian World)
• Vast Beatles museum hailed as 'extraordinary' by Paul McCartney to open in Liverpool in 2028 (Guardian World)
• 'Coral Island' announces major update and Nintendo Switch 2 release (Vice News)
• Obsession Fortnite Skin Revealed – Release Date and Bundle Items Confirmed (Vice News)
• Getting Ziggy with it: David Bowie's alter egos inspire dance show transforming his songs (Guardian World)

**Education and academia**
• La mobilisation étudiante continue, mais reste freinée par les fermetures administratives des universités (Le Monde)

**International conflicts**
• In the Middle East, US military redeployed under fire of Iranian missiles (Le Monde)
• Madagascar, new land of recruitment and influence for Russia (Le Monde)
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
