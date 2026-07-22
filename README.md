# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[July 22, 2026](reports/2026-07-22.md)**

*Last updated: 2026-07-22 12:44 UTC · Generated daily at 6:05 AM EST*

```
July 23, 2026

**Armed conflicts and attacks**
• Trump ally Andy Biggs pledges to "work with people" he disagrees with after winning Arizona primary (Guardian World)
• Iran war costs revealed at $37.5bn as Senator Hegseth warns of "another forever war" (Guardian World)
• Hegseth estimates rising cost of Iran war now at $37.5bn – live coverage (Guardian World)
• Wednesday briefing: Trump's Iran gamble has produced a crisis reshaping the global order (Guardian World)
• Trump's Iran gamble has produced a crisis reshaping the global order (Guardian World)
• Mamdani urges US government to arrest Netanyahu if Israeli PM visits US (Guardian World)
• New York Mayor Zohran Mamdani admits he lacks legal authority to arrest Benjamin Netanyahu (Le Monde)
• Iran's foreign minister describes moment of attack that killed Khamenei (Guardian World)
• Lebanon's southern pilot zones launch as first test of Israel-Hezbollah framework (Le Monde)
• Italy shaken after man dies during police arrest (La Repubblica)
• Zelenskyy fires Ukraine army chief and offers Fedorov "prominent position" (Guardian World)
• Ukraine president holds emergency army leadership meeting after protests (Le Monde)

**Politics and elections**
• Platner Replacement in Maine Has 100 Days to Beat Susan Collins (Bloomberg)
• French lawmakers adopt sweeping social media ban for children under 15 (ABC News)
• France becomes first EU country to ban social media access for under-15s (Guardian World)
• US plans new tariffs on dozens of economies as temporary duties expire (Bloomberg)
• Opposition parties shut down Indian parliament in solidarity with "cockroach" protests (Guardian World)
• India's Cockroach movement protesters show no sign of backing down (Guardian World)
• Australia to warn China it won't be bullied by "provocative" actions as it builds military and nuclear arsenal (Guardian World)
• Budget 2027: Sebastien Lecornu juge le niveau de la dette et du déficit de la France "préoccupant, grave même" (Le Monde)

**Law and crime**
• British woman jailed in Hong Kong after making false rape allegations (Guardian World)
• Court win for low-paid Domino's workers in underpayment class action (Guardian World)
• Michelin-starred restaurant owner in South Korea faces jail over ant dessert (Guardian World)
• World's largest meat company faces legal challenge over green credentials of $6bn global expansion (Guardian World)
• Health worker monitored for Ebola in London hospital after working in DRC (Guardian World)

**International relations**
• Japan-exclusive PlayStation game from 1997 is coming to Nintendo Switch 2 (Vice News)
• ALP announces sweeping changes to student work placements as Gaza war looms large at party conference (Guardian World)
• Norway's national oil company profits double to $11.5bn amid war on Iran (Guardian World)
• Six beluga whales finally leave embattled Canadian marine park (Guardian World)
• People with secret "safe phones" advised to turn off devices during national test of AusAlert emergency warning (Guardian World)
• Spain hotel chain ceases operations in Cuba under pressure from Washington (Guardian World)
• Atlanta rapper Alley Boy passes away at 42 after battling kidney disease (Vice News)
• Italy shaken after man dies during police arrest (La Repubblica)

**Business and economy**
• "He's an analog man in a digital AI world": Nolan's "The Odyssey" made back its $250M budget in 3 days without industrywide AI cost cutting (Fortune)
• Samsung Unpacked 2026: all the news from the July foldable launch (The Verge)
• Louis E. Brus (1943–2026): A consummate physical chemist and pioneer in exploration of spectroscopy of materials at nanoscale (PNAS)
• Prediction of factors contributing to Pain Intensity among low back pain patients: A comparative machine learning frameworks (Random Forest versus XGBoost) (PLOS One)
• Peak Design's modular Field Bracket has a finder tag built-in (The Verge)
• OpenAI admits to unprecedented hack of platform by its own AI agents (Le Monde)

**Science and technology**
• They'll verify. They just won't act. How authority framing and laundered code turn a trusted agentic CI/CD pipeline into an attack surface (arXiv)
• Bidirectional association between cognitive function and depressive symptoms in UK community elderly based on physical activity as mediator (PLOS One)

**Environment**
• Le recul environnemental de trop: Monique Barbut, ministre de la transition écologique, annonce remettre sa démission après le vote de la loi d'urgence agricole (Le Monde)

**Health and medicine**
• Health worker monitored for Ebola in London hospital after working in DRC (Guardian World)

**Culture and entertainment**
• 10 Women in Hip-Hop and R&B Who Deserve More Recognition for Their Contributions to the Genre (Vice News)
• 4 Rock Songs With Opening Lines That Every Millennial Recognizes Immediately (Vice News)
• Cheech & Chong's Mini Blazers Are the Rare Kief-Coated Pre-Rolls That Don't Smoke Like a Mess (Vice News)
• Quit Ruining Your Whiskey. Get a Machine That Makes Big Ice. (Vice News)

**Sports**
• Tour de France 2026: la course contre le temps de l'équipe TotalEnergies, en quête d'un repreneur (Le Monde)

**Social issues**
• Brittany Higgins accuses Pauline Hanson of victim-blaming for calling domestic violence a "two-way street" (Guardian World)
• Hannah Rapp's violent death sparks outpouring of grief (Guardian World)
• Mahmood and Streeting accused of making "cheap jokes" about prisoner early release scheme (Guardian World)
• NHS trust investigated for corporate manslaughter after Nottingham attacks (Guardian World)
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
