# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 7, 2026](reports/2026-11-07.md)**

*Last updated: 2026-11-07 16:49 UTC · Generated daily at 6:05 AM EST*

```
**November 7, 2026**

Armed conflicts and attacks
• Five people killed and more than a dozen injured in a shooting in Kraków, Poland; suspect apprehended (The Guardian, Le Monde)
• Russian strikes on Ukraine’s energy grid cause widespread blackouts and water shortages in Kyiv and other regions (The Guardian, Le Monde)
• French prosecutors open investigation into bomb threats targeting aircraft, examining possible foreign state involvement (Le Monde)
• Former Australian soldier Ben Roberts-Smith partners with gym business selling “war crimes” branded pre-workout supplement (The Guardian)
• Barrister for Russell Brand refers himself to regulatory watchdog following confrontation with Sunday Times journalist (The Guardian)
• Three teenagers arrested after 17-year-old injured in sword attack near school in Gloucester, UK (The Guardian)

Politics and elections
• US midterms: Democrats celebrate victories; Trump names Stephen Miller as incoming chief of staff, pledging “total devotion” (The Guardian, Bloomberg)
• New Zealand election remains “too close to call” days after voting, leaving country facing weeks of uncertainty (The Guardian)
• Paraguay’s ousted president placed under house arrest after banking crisis left 60% of population unable to access accounts (The Guardian)
• UK Home Office sued by advocacy group after stripping nearly 1,500 EU citizens of right to remain in Britain (The Guardian)
• Los Angeles progressives, led by Councilmember Nithya Raman, consolidate influence in city government (The Guardian)
• Jean-Luc Mélenchon launches 2027 French presidential campaign with call to “change everything” at Le Bourget rally (Le Monde)
• Pope Francis says he is “proud to be an American” following US elections, credits God and doctors for health recovery (ABC News)
• French Democrats aim to overhaul US presidential election system following midterm gains (La Repubblica)
• French MP Stéphane Altieri forced to resign as head of anti-corruption agency ANAC over legal incompatibility (La Repubblica)
• Luton Youth Hub opens with £10m funding to support young people into employment and training (GOV.UK)

Business and economy
• Global stocks slide amid “big worries over AI” following Democratic midterm wins, raising regulatory concerns (The Guardian)
• North Korean hackers steal $6 billion from Binance in elaborate scheme involving fake job interview and malware (La Repubblica)
• US Senate plan to fast-track energy permitting heads for legislative showdown (Bloomberg)
• National Trust votes to seek new banking partner better aligned with its environmental policies (The Guardian)
• Climate activists break into Microsoft datacentre construction site in Amsterdam to protest expansion (The Guardian)
• Study finds “high safety” replacement chemicals in plastic food packaging linked to lower birth weights (The Guardian)
• Research in West Africa shows climate and socioeconomic variables can predict low birth weight, enabling early warning systems (PNAS)

Law and crime
• UK Court of Appeal rules against Home Office in case involving asylum seeker kidnapped and held for ransom in Libya (The Guardian)
• Father of Meghan Markle arrested in France on child sexual abuse charges, seven years after initial allegations (Le Monde)
• Parents welcome £10m “life-changing” inclusive play centre for disabled children in the UK (The Guardian)

International relations
• Germany expects to decide on new fighter jet purchase by March, defense minister tells Funke media group (Bloomberg)
• Turkey’s Afşin-Elbistan coal complex continues to cause severe environmental damage as country prepares to host COP31 (Le Monde)
• Identity tensions erupt into street violence in Rouen, France, following two violent attacks (Le Monde)
• Paris demonstrations on November 7 remain “globally calm and controlled,” according to interior ministry (Le Monde)
• US
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
