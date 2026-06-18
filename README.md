# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[June 18, 2026](reports/2026-06-18.md)**

*Last updated: 2026-06-18 14:18 UTC · Generated daily at 6:05 AM EST*

```
**June 18 2026**

---

### Armed conflicts and attacks
- **U.S. President Donald Trump signs a historic US‑Iran peace memorandum, claiming it averts a “worldwide depression.”** The agreement ends a decade‑long proxy war and triggers immediate market optimism. (The Guardian)  
- **Ukrainian forces launch a massive drone strike on a Moscow oil refinery, igniting a fire that the city mayor says is “almost under control.”** It marks the biggest air raid on the Russian capital since the war began. (The Guardian, Le Monde)  
- **Taliban officials in Afghanistan publicly destroy smartphones as part of a new nationwide ban on personal devices.** The decree follows intensified crackdowns on “un-Islamic” technology. (The Guardian)  
- **First Saudi‑flagged supertankers begin transiting the Strait of Hormuz, signalling a shift in regional oil logistics amid the Iran‑Israel‑US stalemate.** (Bloomberg)  
- **Oil prices tumble after the signing of the US‑Iran deal, with analysts warning of volatility in the Middle‑East energy market.** (The Guardian)  
- **Dubai’s residential property market collapses “off a cliff” as foreign investment dries up following the Middle‑East conflict.** (The Guardian)  

### Disasters and accidents
- **Tropical Storm Arthur weakens to a tropical storm as it makes landfall in Texas, bringing heavy rain and localized flooding.** (The Guardian)  
- **England’s Met Office issues amber heat warnings for southern counties, expecting temperatures between 34 °C and 38 °C over the weekend.** (The Guardian)  
- **France experiences a severe heatwave, with temperatures soaring to 38 °C and multiple “Fête de la Musique” concerts cancelled.** (Le Monde)  

### Politics and elections
- **Ireland’s Dáil votes to scrap the three‑day waiting period for abortions, aligning the law with the 2018 referendum.** (The Guardian)  
- **Prominent alumni and staff from Eton College attend the right‑wing “Alliance for Responsible Citizenship” summit in London, sparking debate over elite influence in politics.** (The Guardian)  
- **Australian Prime Minister Anthony Albanese announces generous capital‑gains‑tax exemptions for small businesses after a backlash to his budget.** (The Guardian)  
- **Iceland prepares for a national referendum on EU membership, with polls showing a deeply divided electorate.** (The Guardian)  
- **French left‑wing parties clash after the LFI concert ban at the Fête de la Musique, highlighting internal divisions ahead of upcoming elections.** (Le Monde)  
- **Corsican constitutionalists debate the island’s autonomy in a televised forum, reflecting growing regionalist sentiment.** (Le Monde)  

### Law and crime
- **A Chicago man is charged with a hate crime after setting fire to a cross in a public park, the first such prosecution in the city since 2022.** (The Guardian)  
- **UK teacher Jamie Varley receives a whole‑life order for the sexual abuse and murder of an adopted infant in Preston.** (The Guardian)  
- **Australian media union condemns Pauline Hanson’s “bitter, unprofessional” attack on a Guardian journalist during a National Press Club speech.** (The Guardian)  

### Business and economy
- **Pizza Hut is sold to a consortium of private‑equity firms for $2.7 billion, ending decades of corporate ownership.** (Vice)  
- **Abu Dhabi billionaire “the $1 trillion man” emerges as the UAE’s chief troubleshooter in delicate Iran negotiations.** (Bloomberg)  
- **Anthropic releases a detailed roadmap to improve safety in next‑generation AI models, urging industry‑wide standards.** (Bloomberg)  
- **Macron calls for EU‑wide regulation of cutting‑edge AI systems, warning of “uncontrolled societal impact.”** (Bloomberg)  

### Science and technology
- **NASA’s Fermi telescope detects possible sibling supernova remnants, offering new clues about stellar death cycles.** (NASA)  
- **Hubble Space Telescope images a massive merger of galaxy clusters, providing a rare view of large‑scale cosmic collisions.** (NASA)  
- **Citizen‑science project invites the public to hunt for hidden “cosmic companions” in the Sun’s backyard.** (NASA)  

### Culture and entertainment
- **Rockstar Games confirms the pre‑order launch date for *Grand Theft Auto VI*, reviving anticipation for the franchise’s next chapter.** (Vice)  
- **A leak suggests *Persona 6* development is nearly complete, with screenshots hinting at a new protagonist and setting.** (Vice)  
- **Marvel’s *Spider‑Man 2* receives a surprise in‑game update to celebrate “Brand New Day,” adding new suits and missions.** (Vice)  
- **Aardman Animations celebrates 50 years with a Bristol exhibition showcasing Wallace & Gromit’s legacy.** (The Guardian)  
- **Activision announces ports of *Call of Duty: Black Ops 1* and *2* for modern consoles, reviving the classic titles after 14 years.** (Vice)  
- **Vice revisits a classic *MythBusters* experiment that tested *Seinfeld*’s “double‑dipping” myth, concluding the sitcom’s claim was “kind of vindicated.”** (Vice)  
- **A retrospective on the 35‑year‑old *Simpsons* episode deemed too controversial for streaming highlights evolving broadcast standards.** (Vice)  

---  

*All hyperlinks lead to the original reporting sources.*
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

### Government & Major Feeds (2024)
- NASA — https://www.nasa.gov/rss/dyn/breaking_news.rss
- Government of Canada — https://www.canada.ca/en/news/feed.xml
- Supreme Court of Canada — https://decisions.scc-csc.ca/scc-csc/en/rss/index.do
- White House (USA) — https://www.whitehouse.gov/briefing-room/feed/
- CDC Newsroom (USA) — https://tools.cdc.gov/api/v2/resources/media/403372.rss
- GOV.UK News (UK) — https://www.gov.uk/government/announcements.atom
- Australian Government News — https://www.australia.gov.au/news-media.rss
- Australian Department of Health — https://www.health.gov.au/news/rss
- EU Newsroom — https://ec.europa.eu/commission/presscorner/api/rss/all/en
- United Nations News — https://news.un.org/feed/subscribe/en/news/all/rss.xml
- Associated Press — https://apnews.com/rss/apf-topnews

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
- arXiv — http://export.arxiv.org/rss/cs.AI
- bioRxiv — https://connect.biorxiv.org/biorxiv_xml.php?subject=all

### Industry Feeds
- TechCrunch — https://techcrunch.com/feed/
- Wired — https://www.wired.com/feed/rss
- Ars Technica — https://feeds.arstechnica.com/arstechnica/index
- The Verge — https://www.theverge.com/rss/index.xml
- Engadget — https://www.engadget.com/rss.xml
- Forbes Tech — https://www.forbes.com/technology/feed/
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
