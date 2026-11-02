# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 2, 2026](reports/2026-11-02.md)**

*Last updated: 2026-11-02 20:44 UTC · Generated daily at 6:05 AM EST*

```
**Legible News — November 2, 2026**

---

### Armed conflicts and attacks
• Ukraine war: Russian bombardments in Zaporizhzhia oblast kill at least 26 people, President Zelenskyy says; emergency warning systems reportedly hacked. ([Le Monde](https://www.lemonde.fr/international/live/2026/11/02/en-direct-guerre-en-ukraine-dix-huit-personnes-ont-ete-tuees-par-des-bombardements-russes-dans-l-oblast-de-zaporijia-annonce-volodymyr-zelensky_6803934_3210.html), [Guardian](https://www.theguardian.com/world/live/2026/nov/02/ukraine-russia-emergency-warning-systems-hack-zelenskyy-streeting-eu-latest-news-updates))
• Gulf tension: Qatar leads diplomatic talks with Iran to prevent further U.S. military escalation; oil prices fall on hopes of a breakthrough to end the Iran–U.S. conflict. ([NPR](https://www.npr.org/2026/11/01/nx-s1-6023237/gulf-leaders-meet-in-qatar-in-effort-to-stave-off-new-escalation-in-u-s-and-iran-war), [Guardian](https://www.theguardian.com/business/2026/nov/02/oil-price-falls-amid-hope-of-a-breakthrough-to-end-iran-war))
• Israel: Prime Minister Netanyahu calls for a broad coalition under his leadership, excluding Arab parties, after legislative elections; opposition attempts to form an alternative majority. ([Le Monde](https://www.lemonde.fr/international/article/2026/11/02/legislatives-en-israel-benyamin-netanyahou-appelle-a-une-large-coalition-sous-sa-direction-et-sans-les-partis-arabes-l-opposition-doit-se-reunir-pour-tenter-de-constituer-une-majorite_6805316_3210.html))
• Afghanistan: Women in Herat describe desperate conditions under Taliban rule, saying "the air has been taken from us." ([Le Monde](https://www.lemonde.fr/international/article/2026/11/02/en-afghanistan-a-herat-sous-le-regime-des-talibans-des-femmes-desesperees-l-air-nous-a-ete-retire_6805297_3210.html))
• Germany: Weekend protest violence sparks sharp political debate within the governing coalition. ([Le Monde](https://www.lemonde.fr/international/article/2026/11/02/en-allemagne-les-violences-en-marge-des-manifestations-du-week-end-suscitent-un-vif-debat-politique-au-sein-du-gouvernement_6805312_3210.html))
• France: Interior Minister Laurent Nuñez vows not to renounce "intermediate force" tools such as grenades and tear gas for crowd control. ([Le Monde](https://www.lemonde.fr/politique/article/2026/11/02/maintien-de-l-ordre-laurent-nunez-affirme-qu-il-ne-renoncera-a-aucun-moyen-intermediaire-comme-les-grenades-et-gaz-lacrymogenes_6805314_823448.html))
• Australia: New South Wales
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
