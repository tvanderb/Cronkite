# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 15, 2026](reports/2026-11-15.md)**

*Last updated: 2026-11-15 17:40 UTC · Generated daily at 6:05 AM EST*

```
**Legible News — November 15, 2026**

**Armed conflicts and attacks**
• Saudi Arabia, Qatar, Jordan, and Egypt condemn Iranian strikes on Bahrain as Gulf tensions escalate ([Guardian](https://www.theguardian.com/world/live/2026/nov/15/middle-east-crisis-live-iran-bahrain-strikes-gulf-donald-trump-us-israel-yemen-houthis))
• International Court of Justice to rule on whether Myanmar committed genocide against the Rohingya ([Guardian](https://www.theguardian.com/world/2026/nov/15/myanmar-rohingya-genocide-icj))
• Ethnic minority groups in Wales four times more likely to be targeted by police facial recognition scans, data shows ([Guardian](https://www.theguardian.com/technology/2026/nov/15/ethnic-minorities-wales-police-facial-scans-data))
• Two killed in Leeds after police-pursued car crashes into another vehicle ([Guardian](https://www.theguardian.com/uk-news/2026/nov/15/leeds-car-pursued-by-police-crashes-into-another-vehicle))
• Gender-diverse Australian sailors barred from U.S. submarines under AUKUS pact, documents reveal ([Guardian](https://www.theguardian.com/australia-news/2026/nov/16/gender-diverse-australian-sailors-barred-from-us-submarines-despite-aukus-deal-documents-reveal-ntwnfb))
• Planned asylum seeker detention centre next to Oxfordshire sewage works draws criticism ([Guardian](https://www.theguardian.com/uk-news/2026/nov/15/planned-asylum-seeker-detention-centre-next-to-oxfordshire-sewage-works-criticised))
• Trump administration planning to reimburse doctors treating alleged vaccine injuries ([Guardian](https://www.theguardian.com/us-news/2026/nov/15/vaccine-policy-rfk-jr-trump-administration))

**Disasters and accidents**
• Two planes collide on taxiway at Miami International Airport one day after nationwide FAA grounding ([Guardian](https://www.theguardian.com/us-news/2026/nov/15/miami-airport-planes-collide))
• Five killed in tunnel collision in Cosentino, Italy ([La Repubblica](https://www.repubblica.it/cronaca/2026/11/15/news/scontro_galleria_fiego_vittime_chi_sono-425725111/))

**Politics and elections**
• Andy Burnham pledges early intervention and “benefits backstop” to tackle youth unemployment crisis ([Guardian](https://www.theguardian.com/society/2026/nov/15/no-free-lunch-milburn-mcfadden-kuenssberg-uk-benefits-youth-unemployment-neet))
• Black voters powered Democratic wins in Georgia; now they demand policy action ([Guardian](https://www.theguardian.com/us-news/2026/nov/15/georgia-midterm-elections-black-voters))
• Hundreds of thousands protest in Prague for media freedom ([Guardian](https://www.theguardian.com/world/2026/nov/15/czechia-protest-prague-media-freedom))
• UK government guarantees jobs for 90,000 young people furthest from employment ([GOV.UK](https://www.gov.uk/government/news/90000-young-people-furthest-from-work-to-be-given-guaranteed-job-no-matter-where-they-live))
• Transport Secretary Sean Duffy blames prior administrations and Congress for flight stoppage ([Guardian](https://www.theguardian.com/us-news/2026/nov/15/transportation-secretary-sean-duffy-faa-flight-stoppag))
• Katherine Deves among four NSW upper house candidates announced by One Nation ([Guardian](https://www.theguardian.com/australia-news/2026/nov/15/katherine-deves-among-four-nsw-upper-house-candidates-revealed-by-one-nation-ntwnfb))
• World leaders converge on Asia for back-to-back APEC and ASEAN summits ([Guardian](https://www.theguardian.com/w
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
