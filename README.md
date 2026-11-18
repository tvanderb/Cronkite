# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 18, 2026](reports/2026-11-18.md)**

*Last updated: 2026-11-18 19:22 UTC · Generated daily at 6:05 AM EST*

```
**Legible News — Daily Report**  
**November 18, 2026**

---

### Armed conflicts and attacks
• Israel delays construction contracts for the E1 West Bank settlement after the UK imposes sanctions on settler groups. ([The Guardian](https://www.theguardian.com/world/2026/nov/18/israel-construction-contracts-e1-west-bank-settlement-uk-sanctions))  
• Palestinian woman shot dead by Israeli settlers near Jericho, West Bank, according to witnesses. ([The Guardian](https://www.theguardian.com/world/2026/nov/17/palestinian-woman-shot-dead-israeli-settlers-near-jericho-witnesses-say))  
• Israeli parliament elects new Knesset speaker backed by Netanyahu’s opponents, signaling a shift in legislative dynamics. ([The Guardian](https://www.theguardian.com/world/2026/nov/17/israeli-parliament-elects-new-knesset-speaker-backed-netanyahus-opponents))  
• Australia sanctions Daniella Weiss, described as the “godmother” of illegal West Bank settlement expansion, along with a construction company. ([The Guardian](https://www.theguardian.com/world/2026/nov/18/australia-sanctions-construction-company-west-bank-settlement-expansion-ntwnfb))  
• European Court of Auditors urges the EU’s 27 member states to act quickly to defuse the “ticking time bomb” of PFAS pollution. ([Le Monde](https://www.lemonde.fr/planete/article/2026/11/18/pfas-la-cour-des-comptes-europeenne-exhorte-les-vingt-sept-a-agir-vite-pour-desamorcer-cette-bombe-a-retardement_6813164_3244.html))  
• NGOs condemn Russian and U.S. positions on autonomous weapons systems that operate without human intervention, during UN talks in Geneva. ([Le Monde](https://www.lemonde.fr/international/live/2026/11/18/en-direct-guerre-en-ukraine-des-ong-denoncent-les-positions-russes-et-americaines-au-sujet-des-armes-autonomes-qui-fonctionnent-sans-intervention-humaine_6810982_3210.html))  
• Moscow accuses France of direct participation in the war in Ukraine following reports of a secret French military mission to train Ukrainian troops. ([La Repubblica](https://www.repubblica.it/esteri/2026/11/18/news/missione_segreta_soldati_francesi_ucraina_addestramento_truppe_armi_mosca_attacca_partecipazione_diretta_guerra-425731459/))  
• One Nation party’s plan to slash Australia’s refugee intake denounced as having “devastating consequences” by human rights groups. ([The Guardian](https://www.theguardian.com/australia-news/2026/nov/18/one-nation-refugee-intake-immigration-ntwnfb))  
• Man charged in connection with a bomb threat at an ethanol plant in Illinois. ([The Guardian](https://www.theguardian.com/us-news/2026/nov/18/illinois-ethanol-plant-bomb-threat-charges))  
• European Commission accused of “sugarcoating” human rights figures to justify releasing funds to Egypt. ([The Guardian](https://www.theguardian.com/world/2026/nov/18/european-commission-accused-sugarcoating-figures-egypt-loans))  
• Strike risk grows at the busiest U.S. ports as contract negotiations between dockworkers and employers stall. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-11-18/strike-risk-grows-at-busiest-us-ports-as-contract-talks-stall))  
• Caribbean nations warn of severe economic fallout if the EU forces the shutdown of citizenship-by-investment programs. ([The Guardian](https://www.theguardian.com/world/2026/nov/17/st-kitts-nevis-citizenship-investment))

---

### Politics and elections
• Democrats nominate Hakeem Jeffries as the first Black candidate for U.S. House Speaker, despite reservations from progressive lawmakers. ([The Guardian](https://www.theguardian.com/us-news/2026/nov/18/hakeem-jeffries-house-speaker-nomination))  
• Senate committee rejects Trump’s nominee to lead the National Science Foundation. ([The Guardian](https://www.theguardian.com/us-news/2026/nov/18/trump-national-science-foundation-nominee))  
• UK Labour Party faces a double blow over fossil fuel projects as SSE threatens to close a Yorkshire gas storage site without government intervention. ([The Guardian](https://www.theguardian.com/business/2026/nov/18/sse-threatens-to-close-yorkshire-gas-storage-site-unless-ministers-intervene))  
• Andy Burnham, Mayor of Greater Manchester, considers cutting national insurance contributions to fund youth job creation, following the Milburn report. ([The Guardian](https://www.theguardian.com/society/2026/nov/18/burnham-cuts-national-insurance-youth-jobs-milburn-report))  
• UK government unveils draft “relationship reset” with the EU, covering cheese exports, pet passports, and a youth mobility scheme. ([The Guardian](https://www.theguardian.com/politics/2026/nov/18/uk-eu-relationship-reset-draft-explainer))  
• Fears grow that the U.S. may sanction International Court of Justice judges following the Myanmar genocide ruling, which also implicated Israel. ([The Guardian](https://www.theguardian.com/world/2026/nov/18/us-sanctions-icj-judges-myanmar-genocide-ruling-israel-gaza-court))  
• Pakistani man sentenced to 27 years in a U.S. prison for plotting to assassinate Donald Trump. ([The Guardian](https://www.theguardian.com/us-news/2026/nov/17/pakistani-man-jailed-trump-murder-plot))  
• Isolated Indigenous tribe in the Brazilian Amazon makes contact, raising alarms over threats to their territory and way of life. ([The Guardian](https://www.theguardian.com/world/2026/nov/17/brazil-amazon-isolated-indigenous-people))  
• French National Assembly votes to lift the ban on renting out energy-inefficient “thermal sieves,” sparking heated debate over the housing crisis. ([Le Monde](https://www.lemonde.fr/societe/article/2026/11/18/suppression-de-l-interdiction-de-louer-les-passoires-thermiques-a-l-assemblee-fortes-tensions-sur
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
