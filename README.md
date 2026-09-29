# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[September 29, 2026](reports/2026-09-29.md)**

*Last updated: 2026-09-29 16:51 UTC · Generated daily at 6:05 AM EST*

```
September 30, 2026

Armed conflicts and attacks
• Estonian authorities blame Russia for an arson attack on a drone manufacturer that supplies Ukraine (Guardian World)
• Questions remain over Iran's connection to an alleged RAF Fairford bomb plot (Guardian World)
• Israel: Poison traces found on Netanyahu's travel documents to UAE, official says; UAE leader asked Netanyahu to be excused (La Repubblica)
• Russian forces tell NATO: "We will defend Kaliningrad with full arsenal" amid Ukraine war developments (La Repubblica)
• Pope Leo XIV states: "AI and wars, we cannot stand by. Dialogue is needed" regarding extremist trends (La Repubblica)

Disasters and accidents
• Body of newborn baby discovered on Welsh shoreline, prompting search for mother (Guardian World)
• New York man killed after bag caught in subway train doors (Guardian World)

Politics and elections
• Australia concedes no scientific consensus on social media harms for teenagers, but 'credible risks' justify ban (Guardian World)
• Spanish government approves measures to ease housing crisis amid outcry over eviction of 87-year-old (Guardian World)
• Guardian Essential poll: Australia's Coalition primary vote sinks to lowest ever as majority support hardline immigration policies (Guardian World)
• US Senator blocks bill to prohibit Trump from demolishing Kennedy Center without Congressional approval (Guardian World)
• Trump set to host Nvidia and Anthropic CEOs to discuss AI risks (Bloomberg)
• UK's Burnham states Brexit has done more harm than good in revolutionary and left-wing speech (Bloomberg)
• French students and police clash as school blockades turn violent (Guardian World)
• European Commission outlines five-point plan to strengthen resilience and security of EU external borders (Government EU Newsroom)
• European Parliament inaugurates David Maria Sassoli building amid discussions on EU future (Government EU Newsroom)
• Germany's AfD proposes economic forum with Russia and USA in 2027 to reopen Nord Stream (La Repubblica)
• Italy: Gasoline prices capped as Q8 accepts government price cap invitation (La Repubblica)
• Italy: Gianni Di Vita's clinics raided in poisoning case; wife's bag seized (La Repubblica)
• September 29 strike in France: over 200,000 people demonstrated demanding increased funding for public sector (Le Monde)

Law and crime
• Lindsay Clancy returns to court after Massachusetts murder case mistrial (Guardian World)
• Trump administration asks Supreme Court to allow denial of gender-affirming care to transgender prisoners (Guardian World)
• Violent interpellation in Corbeil-Essonnes: new video contradicts police version (Le Monde)
• Italy: Poisoning investigation of Gianni Di Vita continues; wife's bag seized (La Repubblica)

Business and economy
• Iran's currency hits new record low as it accuses US of seeking to turn Iran "back into a colony" (Industry Fortune)
• Mumps vaccine study evaluates real-world protective effect among children under 15 in Taizhou (Academic PLOS One)
• Family moves to small Maine island after finding $1,000/month house deal (Business Insider)
• Small business owner reports $2,000 per person Greece trip was worth six-figure revenue boost (Business Insider)
• Individual chooses Columbia over UPenn scholarship, questions decision (Business Insider)
• South West Water fined £8m for hundreds of sewage spills in Cornwall and Devon (Guardian World)
• Soho House launches investigation after out-of-date food mislabeled in Shoreditch kitchen (Guardian World)
• Targeted left ventricular lead placement trial in heart failure patients published in Denmark (Academic The Lancet)

International relations
• Ethiopia accuses Eritrea, Sudan, and Egypt of supporting rebels (Le Monde)
• Eiffel Tower chief to step down after excluding female staff during Hindu delegation visit (ABC News)
• France: More than 200,000 people protested September 29 demanding increased public sector funding (Le Monde)
• Gaza: Israeli army describes "targeted factories" and "collateral damage" methods (Le Monde)
• Eiffel Tower director Patrick Branco Ruivo announces departure after female staff exclusion controversy (Le Monde)
• Contraceptive pill alert: Health concerns over desogestrel causing patient anxiety and treatment interruptions (Le Monde)
• Italy: September 29 strike with 200,000+ protesters demanding more public funding (Le Mode)
• India: Safety burden for sexual assault cannot fall on women from Jamui to Delhi (Guardian World)
• New AI trends emerge: "Weaponized Pooping" becoming internet sensation (Vice News)
• "Grandmaslop" AI family photo trend freaks out internet (Vice News)
• Scientific evidence supports "sleep on it" advice for decision-making (Vice News)
• Gen Z expects millennials to retire so they can have jobs (Vice News)
• Heroes of the Storm adds new character after nearly six-year hiatus (Vice News)
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
