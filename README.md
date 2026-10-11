# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 11, 2026](reports/2026-10-11.md)**

*Last updated: 2026-10-11 16:39 UTC · Generated daily at 6:05 AM EST*

```
**October 11, 2026**

---

### Armed conflicts and attacks

• Houthi rebels claim responsibility for missile attack on Riyadh’s King Khalid International Airport that killed 12 people and wounded over 300; Saudi authorities confirm casualties and vow response ([Guardian](https://www.theguardian.com/world/live/2026/oct/11/saudi-arabia-riyadh-airport-houthis-yemen-attack-blockade-trump-latest-news-updates), [NPR](https://www.npr.org/2026/10/10/g-s1-147682/attack-on-riyadh-airport-killed-12-people-and-wounded-over-300-more-saudi-authorities-say), [Le Monde](https://www.lemonde.fr/international/article/2026/10/11/arabie-saoudite-nouvelle-attaque-contre-l-aeroport-de-riyad-au-lendemain-de-frappes-imputees-aux-houthistes-ayant-fait-12-morts_6791939_3210.html))

• Donald Trump announces surprise “energy ceasefire” between Russia and Ukraine halting strikes on energy infrastructure for 60 days; Volodymyr Zelenskyy says he was not informed in advance but signals willingness to accept if Putin agrees, and suggests he would call elections under a truce ([Guardian](https://www.theguardian.com/us-news/live/2026/oct/11/donald-trump-ukraine-russia-energy-ceasefire-diesel-latest-updates), [Le Monde](https://www.lemonde.fr/international/live/2026/10/11/en-direct-guerre-en-ukraine-c-est-aux-ukrainiens-de-choisir-leur-dirigeant-dit-volodymyr-zelensky-en-reponse-a-donald-trump_6791198_3210.html), [La Repubblica](https://www.repubblica.it/esteri/2026/10/11/diretta/guerra_ucraina_russia_news_oggi-425640146/))

• Escalating clashes between Pakistan and Afghanistan along their shared border cause heavy civilian casualties and displacement; both sides accuse the other of cross-border shelling ([Le Monde](https://www.lemonde.fr/international/article/2026/10/11/entre-le-pakistan-et-l-afghanistan-une-escalade-aux-lourdes-consequences-humaines_6791923_3210.html))

• Canadian military faces growing difficulty defending the vast Arctic territory as melting ice opens new routes and strategic competition intensifies; officials cite insufficient icebreakers, surveillance, and personnel ([Le Monde](https://www.lemonde.fr/international/article/2026/10/11/au-canada-l-armee-confrontee-a-la-difficile-defense-de-l-immense-territoire-arctique_6791928_3210.html))

• Former SAS soldier Ben Roberts-Smith attends Canberra ceremony honoring Australian troops who served in Afghanistan, his first major public appearance since losing defamation case over war crimes allegations ([Guardian](https://www.theguardian.com/australia-news/2026/oct/11/ben-roberts-smith-attends-canberra-event-honouring-australian-troops-who-served-in-afghanistan-ntwnfb))

• Experts warn Trump-Putin energy deal will have minimal impact on U.S. diesel prices, citing global market dynamics and limited Russian refining capacity ([Guardian](https://www.theguardian.com/us-news/2026/oct/11/trump-russia-diesel-deal-putin-little-impact-prices))

• U.S. defense policies hinder European allies’ efforts to build autonomous military capabilities while simultaneously pressuring them to increase spending, French analysis finds ([Le Monde](https://www.lemonde.fr/international/article/2026/10/11/defense-tout-en-attendant-des-europeens-qu-ils-augmentent-leurs-capacites-les-etats-unis-entravent-les-efforts-de-leurs-allies_6791306_3210.html))

---

### Disasters and accidents

• Panama declares state of emergency after magnitude 6.3 earthquake and persistent aftershocks rattle communities, damaging hundreds of homes and cutting power and water in Chiriquí province ([Guardian](https://www.theguardian.com/world/2026/oct/11/panama-eathquake-state-of-emergency))

• Tropical Storm Isaias leaves thousands without power across Florida and Alabama as it moves north; utilities warn restoration could take days in hardest-hit coastal areas ([Guardian](https://www.theguardian.com/world/2026/oct/11/isaias-florida-alabama-power-outages))

• Missing Australian hiker Jordan Yap, 28, found dead on remote trail in Peru’s Cordillera Huayhuash after week-long search; authorities believe he fell while attempting a high-altitude crossing ([Guardian](https://www.theguardian.com/australia-news/2026/oct/11/missing-australian-hiker-jordan-yap-last-seen-on-remote-trail-found-dead-in-peru))

• Flu cases in England running significantly above seasonal norms for September, UK Health Security Agency reports; early surge prompts calls for accelerated vaccination campaign ([Guardian](https://www.theguardian.com/society/2026/oct/11/flu-season-early-rise-september-england-vaccination-jab-ukhsa))

---

### Politics and elections

• Raphaël Glucksmann wins French left-wing presidential primary outright with 66% of first-round vote, avoiding runoff; will represent unified left in 2027 election against Macron’s centrist camp and far right ([Le Monde](https://www.lemonde.fr/election-presidentielle-2027/live/2026/10/11/en-direct-primaire-a-gauche-qui-de-raphael-glucksmann-olivier-faure-segolene-royal-emmanuel-maurel-ou-jerome-guedj-va-se-qualifier-pour-le-second-tour-suivez-les-resultats-du-premier-tour_6791926_6205049.html))

• Donald Trump publicly urges Senator John Fetterman to switch from Democratic to Republican Party, praising his “common sense” on trade and Israel; Fetterman dismisses overture ([Guardian](https://www.theguardian.com/us-news/2026/oct/11/trump-john-fetterman))

• UK government struggles to curb English Channel small-boat crossings as
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
