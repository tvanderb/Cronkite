# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 13, 2026](reports/2026-10-13.md)**

*Last updated: 2026-10-13 18:07 UTC · Generated daily at 6:05 AM EST*

```
**October 14, 2026**

**Armed conflicts and attacks**
• Saudi Arabia struck strategic oil depots near Yemen's capital in a military operation (Guardian World)
• Russia attempted to interfere in the 2016 Brexit referendum, MI5 confirms (Guardian World)
• Texas man was run over by ICE agents who were allegedly chasing someone else (Guardian World)
• Five people killed when Hurricane Simon and Tropical Storm Rachel hit Mexico's Pacific coast (Guardian World)
• Rapper-Wrestler lost his job after performing a controversial freestyle about deadly attacks (Vice News)

**Disasters and accidents**
• Indonesia wildfire sparked by El Niño razed almost 300 homes (Guardian World)
• Argentina temporarily closed Iguazu Falls following El Niño-fueled surge in water levels (Guardian World)
• Flying foxes in New South Wales and Victoria face mass starvation due to food shortages (Guardian World)

**Politics and elections**
• Elon Musk became the largest donor of the 2026 midterm election cycle with $366 million spent (Guardian World)
• AI Anxiety Collides With the Midterms as voters express concerns about artificial intelligence's role in society (Bloomberg)
• Germany and Ukraine jointly demanded a ceasefire for the entire energy sector (Bloomberg)
• UK bird populations fell to lowest level on record, prompting conservation concerns (Guardian World)
• India's contentious electoral revision sparked protests and outrage over alleged manipulation (Guardian World)
• French high school students mobilized 480,000 people nationally, with 161,500 demonstrating in Paris (Le Monde)
• France's National Assembly unanimously adopted comprehensive legislation against gender-based violence (VSS law) (Le Monde)
• Canada's Prime Minister Carney emphasized national unity as Alberta referendum approaches (ABC News)

**Law and crime**
• The FTC and seven U.S. states sought contempt ruling against Martin Shkreli regarding pharmaceutical ban (Guardian World)
• Kimberly Guilfoyle denied allegations of misconduct while resigning as U.S. ambassador to Greece (Guardian World)
• Florida carried out execution despite scrutiny over previous botched Tennessee attempt (Guardian World)
• Hundreds of early-release prisoners in England and Wales were not being properly tagged, MPs report (Guardian World)
• French actor Francis Renaud was detained for rape, harassment, and violence charges (Le Monde)
• Child safety staff were determined to send Elizabeth Struhs home with parents despite medical concerns, inquest hears (Guardian World)
• Australian politician Anne Aly revealed receiving 19 death threats in one week (Guardian World)
• Norway man died after walking from Canada to Alaska with his dog, found dead just steps from his destination (La Repubblica)
• Former French Prime Minister François Fillon's alibi was questioned in ongoing investigation, plaintiff publishes book (Le Mode)

**International relations**
• UK requested Interpol to reject Argentina's 'politically motivated' requests for Falklands oil arrests (Guardian World)
• UK committed to respecting and defending rights of Overseas Territories populations, statement at UN Fourth Committee (Government GOV.UK News)
• Britons traveling to EU countries were advised not to apply for delayed ETIAS visa waiver (Guardian World)
• UK bird populations fell to lowest level on record (Guardian World)
• UK Statement at UN Fourth Committee on Overseas Territories' right to self-determination (Government GOV.UK News)

**Business and economy**
• New study protocol evaluates effectiveness and cost-benefit of worksite mental health program among manufacturing workers (PLOS One)
• Research on low peak expiratory flow and subsequent lung disease diagnosis in Health and Retirement Study participants (PLOS One)
• Self-management intervention effectiveness studied for type 2 diabetes patients at high risk for kidney disease (PLOS One)
• Interactive effects of seed rate, sowing method, and variety on teff yield analyzed in Ethiopian highlands (PLOS One)
• PAGE Framework developed for studying comics at scale using artificial intelligence (arXiv)
• Knowledge, willingness, and self-efficacy in CPR studied among Malaysian tertiary institution participants (PLOS One)
• Xteink X4 Pro e-reader reviewed as compact device available at reduced price (The Verge)
• Fortnite announced new sprites coming in October 15 update (Vice News)

**Technology**
• FTC and seven states sought contempt ruling against Shkreli over pharmaceutical ban (Guardian World)
• AI Anxiety Collides With the Midterms as artificial intelligence impacts political landscape (Bloomberg)

**Environment**
• UK bird populations fell to lowest level on record according to new environmental study (Guardian World)
• Flying foxes in NSW and Victoria face mass starvation amid food shortages (Guardian World)
• Indonesia wildfire fueled by El Niño razes almost 300 homes (Guardian World)
• Connected glasses regulation requires EU to make recording functions clearly visible for privacy protection (Le Mode)

**Culture**
• Dungeons and Dragons Modern Horror Adventure adds new playable species and four backgrounds (Vice News)
• Tove Lo discussed high-energy crowds and evolved sound at Portola 2026 Festival (Vice News)
• Tom Morello recalled forbidden guitar techniques with late Randy Rhoads (Vice News)
• Tupac Shakur's convicted killer faces life sentence over 30 years after rapper's murder (Vice News)

**Education**
• French high school movement mobilized 480,000 students nationwide, with 161,500 in Paris alone (Le Monde)

**Health**
• Worksite mental health program effectiveness evaluated among manufacturing workers (PLOS One)
• Self-management intervention studied for clinical outcomes in type 2 diabetes patients (PLOS One)
• Low peak expiratory flow linked to first self-reported lung disease diagnosis (PLOS One)
• CPR knowledge and self-efficacy studied in Malaysian tertiary institutions (PLOS One)
• Murine monocyte-derived dendritic cells showed unique identity compared to other phagocytes (bioRxiv)

**Sports**
• AFL instructed Sportsbet to cease using players in AI-generated content (Guardian World)
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
