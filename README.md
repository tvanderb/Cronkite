# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 23, 2026](reports/2026-10-23.md)**

*Last updated: 2026-10-23 15:42 UTC · Generated daily at 6:05 AM EST*

```
**October 23, 2026**

**Armed conflicts and attacks**
• Russia and Ukraine agree to local ceasefire in Oleshky amid deepening humanitarian crisis, with ongoing Starlink satellite network disruptions reported (Guardian World)
• Netanyahu orders "very extensive" operation in West Bank after two Israeli soldiers killed, subsequently closing West Bank following attacks in Hebron (Guardian World, NPR World)
• Magnitude-7 earthquake hits Tibet, killing at least 16 and destroying hundreds of homes (Guardian World)
• El Salvador deploys special forces to Haiti to locate four missing soldiers who came under attack (ABC News)
• French police open fire on attackers at concerts in Trappes and La Verrière, resulting in one death and four injuries in automatic weapon incident (Le Monde)

**Disasters and accidents**
• Storm Austen leaves 289,000 private households without electricity across 23 departments in north and west France on red alert (Le Monde)
• Thousands of homes without power as Storm Austen hits south-west England (Guardian World)
• Magnitude-7 earthquake in Tibet kills at least 16 and destroys hundreds of homes (Guardian World)
• Ebola outbreak in Nigeria raises concerns about virus spread from Swiss patient linked to DR Congo (Guardian World)

**Politics and elections**
• Brazil's Lula and Bolsonaro tied heading into runoff election, with Lula opening state toolbox to woo voters on social programs and economic initiatives (Bloomberg, ABC News)
• US Supreme Court sides with Republicans on rejecting student IDs in New Hampshire midterms (Guardian World)
• Brazil election battle for the Amazon highlighted in podcast discussion (Guardian World)
• India slashes cost of cancer drugs after court rules price mark-ups are "extortion" (Guardian World)
• Musk giving tops $445 million in final midterm election push for GOP candidates (Bloomberg)
• UK government to make unprecedented intervention in setting of water bills amid investment concerns (Guardian World)
• Jim Chalmers faces difficult economic choices where solving one problem worsens another (Guardian World)
• Reform Party Farage donor reveals business ties to foundation linked to Iranian regime (Guardian World)
• CFTC Chair discusses prediction markets, election implications, and oil trading trends (Bloomberg)
• Why the anti-Trump playbook is failing in Canada's timber country (Bloomberg)

**Economy and business**
• Oil prices rise above $115 a barrel amid fears US will renew strikes on Iran (Guardian World)
• UK government intervention in water bills raises questions about utility pricing and investment (Guardian World)
• Australia's Jim Chalmers faces economic policy challenges balancing competing priorities (Guardian World)
• Billionaire Olivier Bouygues convicted of two years suspended prison for destroying protected bird species (Le Monde)
• French water bill pricing to be subject to unprecedented government intervention (Le Monde)

**Law and crime**
• US supreme court rules against accepting student IDs in New Hampshire midterms (Guardian World)
• Trump ordered to sit for deposition in $10 billion defamation lawsuit against BBC (NBC News)
• Beau Lamarre-Condon allegedly confessed to friend about killing, asking for help cleaning "mess" during murder trial (Guardian World)
• Mother sought advice from Alan Jones after broadcaster's alleged indecent assault of her son, court hears (Guardian World)
• Trump's top border official defends Big Bend border wall plan despite mounting opposition (Guardian World)

**International relations**
• Beetlejuice Fortnite skin revealed with release date and pricing details (Vice News)
• Scientists discover potential best source of protein on Earth that is not meat (Vice News)
• Mystery over source of Ebola infection in Nigeria fuels concern about virus spread (Guardian World)
• Finland's 24-hour newborn puppy livestream becomes TV smash hit (Guardian World)
• Petrolina, Brazil faces "tsunami of mountains" seismic activity with earthquake fears in Palermo area (La Repubblica)
• El Salvador deploys special forces to Haiti for military assistance mission (ABC News)
• UK government prepares citizens with survival guide including three-day supplies, cash, and radio (La Repubblica)
• Pope Francis cancels visit to Assisi on doctor's advice, prepares for Latin America trip (La Repubblica)
• Protests and roadblocks removed in Campania and Calabria, authorities declare return to normalcy (La Repubblica)

**Science and health**
• Study finds perceived social support impacts college athletes' academic burnout with cognitive reappraisal as moderating factor (PLOS One)
• Research identifies potential new anti-aging beauty treatment derived from human remains (Vice News)
• Phase 3 clinical trial shows efficacy and safety of mitapivat for sickle cell disease patients (The Lancet)
• Digital media use presents public health challenges for children and adolescents, according to new framework (The Lancet)
• Altered sperm DNA methylation provides epigenetic pathway from overweight and older fathers to intergenerational disease transmission (PNAS)

**Culture and society**
• Cardi B reveals fatigue with feuding against female rappers, calls it "kinda boring" (Vice News)
• Eight Gen Z dating trends that millennials strongly dislike emerge in social research (Vice News)
• "Chatfishing" phenomenon spreading on dating apps raises new concerns (Vice News)
• Finnish 24-hour newborn puppy livestream captures global attention as television sensation (Guardian World)
• Italian families abandon victims: 80,000 euros spent on Mattia case with no justice achieved (La Repubblica)

**Environment**
• Europe records 50,000 deaths this summer from heat waves, with Italy ranking first and Milan setting records (La Repubblica)
• Scientists warn we have entered new glacial era as global warming halts, based on recent findings (La Repubblica)
• Nepal refuses to rebuild roads in same locations after mountain tsunami, citing population relocation needs (Le Mode)
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
