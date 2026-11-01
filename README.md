# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[November 1, 2026](reports/2026-11-01.md)**

*Last updated: 2026-11-01 17:07 UTC · Generated daily at 6:05 AM EST*

```
The user wants me to create a daily news report in the style of Legible News. I need to:

1. Group stories by category
2. Each story as a single bullet point with headline, key details, source citation
3. Merge duplicate stories from multiple sources
4. Choose most relevant category for each story
5. Use clean, factual, neutral language
6. Include hyperlinks from provided URLs
7. Focus on most significant/recent stories
8. Mix of sources and regions
9. 45-65 total stories
10. Start with today's date (which appears to be November 1, 2026 based on the article dates)

Let me first organize the stories by category and identify duplicates/related stories.

Looking at the data, I see many stories from Guardian, Bloomberg, Le Monde, etc. Let me categorize them properly.

First, let me list all stories with their categories from the data:

1. Michael Dell story - Business and economy (Fortune)
2. Stellantis AI push - Business and economy (Fortune)
3. AI Concerns in midterm campaigns - Politics and elections (Bloomberg)
4. Traders on Kalshi/Polymarket in Maine - Politics and elections (Bloomberg)
5. Iran's Long Game complicates Trump war plans - Armed conflicts and attacks (Bloomberg)
6. Petrol bomb thrown at French riot police - Armed conflicts and attacks (Guardian)
7. UK statement at UN Security Council - Politics and elections (Gov.uk)
8. Tens of thousands protest against Modi in Delhi - Politics and elections (Guardian)
9. Michael Mann shoots himself - Disasters and accidents (Guardian)
10. Rep. DeLauro on cost of living - Armed conflicts and attacks (Bloomberg) - wait, this is categorized as Armed conflicts but seems like Politics
11. Superior Frontal Gyrus study - Business and economy (bioRxiv) - this seems like science/health
12. Welsh health board closing urgent care - International relations (Guardian) - should be Health
13. GTA 6 fans missing work - Business and economy (MarketWatch)
14. Former NSW Liberal overhaul One Nation - Politics and elections (Guardian)
15. Trump banks on rallies - Armed conflicts and attacks (Bloomberg) - should be Politics
16. Five teenagers hurt in stabbing Hampshire - International relations (Guardian) - should be Crime/Law
17. Multiple shootings in Dallas - International relations (Guardian) - should be Armed conflicts
18. Kanye West challenged Paul McCartney - International relations (Vice) - should be Culture/Arts
19. Quit dream job at 27 - Business and economy (Business Insider)
20. Airline hack Iceland stopover - Business and economy (Business Insider)
21. Binance resumes withdrawals after $6.3bn hack - Business and economy (Guardian)
22. Cambridge scientist died in Spain train crash - Armed conflicts and attacks (Guardian) - should be Disasters
23. Rightwing racism stirs South Asian mobilization in Texas - Politics and elections (Guardian)
24. Fortnite Pirate Shop Token - Armed conflicts and attacks (Vice) - should be Gaming/Tech
25. Texas data center divides Trump camp - International relations (Le Monde)
26. Digital inheritance after death - International relations (La Repubblica)
27. EU joint statement on crimes against journalists - Politics and elections (EU Newsroom)
28. Home values fall in Australia - Armed conflicts and attacks (Guardian) - should be Business/Economy
29. NT water plan condemned - Armed conflicts and attacks (Guardian) - should be Environment
30. William Nordhaus dies at 85 - International relations (Le Monde) - should be Obituaries/Science
31. My Chemical Romance reunion - International relations (Vice) - should be Culture/Arts
32. Tusk defends Poland constitutional court overhaul - Law and crime (Guardian)
33. Shooting outside Magic City Classic in Alabama - International relations (Guardian) - should be Armed conflicts
34. "Guerre hybride" expression - International relations (Le Monde)
35. Manifestations Oct 31 - investigation for attempted homicide after Molotov cocktail - Armed conflicts and attacks (Le Monde)
36. South Korea seniors using AI dolls - International relations (Le Monde) - should be Society/Tech
37. French administration confronts antisemitic past - International relations (Le Monde)
38. François Guillemot interview - International relations (Le Monde)
39. Lucie family secret - International relations (Le Monde)
40. Manifestations in Germany - International relations (Le Monde)
41. Psychologist on happiest couples - Business and economy (CNBC)
42. Jacinda Ardern in Sydney - Business and economy (Guardian)
43. UK Defence Minister stockpiling food - International relations (La Repubblica)
44. Vannacci donations - International relations (La Repubblica)
45. France indecisive before 2027 presidential - International relations (Le Monde)
46. Lio singer interview - International relations (Le Monde)
47. Asylum seekers sent to France under "one in one out" - Politics and elections (Guardian)

Many of these categories seem misassigned in the original data. I need to re-categorize them properly for a news report. Legible News likely uses standard categories like:
- World / International
- Politics
- Business / Economy
- Technology
- Science / Health
- Culture / Arts
- Sports
- etc.

But the user said to group by category using the categories provided (Armed conflicts and attacks, Disasters and accidents, Politics and elections, Law and crime, etc.). However, many stories are miscategorized. I should use the categories as they make sense for a news report, not necessarily the provided category field which seems noisy.

Let me re-categorize properly:

**Armed conflicts and attacks:**
- Iran's Long Game Complicates Trump's War Plans (Bloomberg)
- Petrol bomb thrown at French riot police / Molotov cocktail on gendarmes in Paris (Guardian + Le Monde - same event)
- Multiple shootings in Dallas leave four dead, 15 injured (Guardian)
- Shooting outside Magic City Classic in Alabama (Guardian)
- Attempted murder probe after petrol bomb thrown at French riot police (Guardian) - same as above
- Manifestations du 31 octobre: enquête ouverte pour tentative d'homicide (Le Monde) - same event

**Disasters and accidents:**
- Director Michael Mann accidentally shoots himself in leg at gun range (Guardian)
- Tributes paid to Cambridge scientist who died in Spain train crash (Guardian)

**Politics and elections:**
- AI Concerns Move to Center of Midterm Campaigns (Bloomberg)
- Traders on Kalshi and Polymarket Went to Maine Hunting a Midterm Election Edge (Bloomberg)
- UK statement at UN Security Council (Gov.uk)
- Tens of thousands protest against Narendra Modi regime in Delhi (Guardian)
- Rep. DeLauro Sees Cost of Living Fueling Democratic Gains (Bloomberg)
- Former NSW Liberal leads overhaul of One Nation candidate selection process (Guardian)
- Trump Banks on Rallies to Turn Out MAGA Faithful One More Time (Bloomberg)
- 'There's a lot of hate': rightwing racism stirs south Asian mobilization in Texas (Guardian)
- Joint statement by EU officials on International Day to End Impunity for Crimes against Journalists (EU Newsroom)
- Asylum seekers still being sent to France under 'one in one out' weeks after scheme ended (Guardian)
- Tusk defends overhaul of Poland's constitutional court despite protests (Guardian) - also Law and crime
- Manifestations en Allemagne: la gauche condamne les violences (Le Monde)
- « Je crois que je vais donner procuration à mes enfants »: France indecisive before 2027 presidential (Le Monde)
- UK Defence Minister stockpiling food (La Repubblica)

**Law and crime:**
- Five teenagers hurt in stabbing at Halloween party in Hampshire (Guardian)
- Tusk defends overhaul of Poland's constitutional court despite protests (Guardian) - could go here or Politics

**Business and economy:**
- Michael Dell turned $1,000 into $302 billion company (Fortune)
- Stellantis AI push: 'best thing for career is to make yourself redundant' (Fortune)
- Superior Frontal Gyrus Cortical Thickness study (bioRxiv) - this is science, not business
- Grand Theft Callout: GTA 6 fans missing work on release day (MarketWatch)
- At 27, I quit my dream job without a plan (Business Insider)
- Airline hack to turn layover into mini trip to Iceland (Business Insider)
- Binance resumes customer withdrawals after record $6.3bn hack (Guardian)
- Home values fall for seventh consecutive month in Australia (Guardian)
- I'm a psychologist who studies couples: happiest relationships do 1 thing differently (CNBC)
- Jacinda Ardern advises politicians to 'rebuild trust by building financial security' (Guardian)

**Science / Health:**
- Superior Frontal Gyrus Cortical Thickness Mediates Association Between Openness to Experience and Theory of Mind (bioRxiv)
- Welsh health board considers closing urgent primary care centres at three hospitals (Guardian)
- South Korea seniors using AI dolls to combat loneliness (Le Monde)

**International relations / World:**
- Texas data center project divides Trump camp (Le Monde)
- Digital inheritance: what happens to data after death (La Repubblica)
- « Guerre hybride » expression considered euphemism by Europeans (Le Monde)
- French administration confronts its antisemitic past (Le Monde)
- François Guillemot interview (Le Monde)
- Lucie family secret (Le Monde)
- Vannacci donations to Futuro Nazionale (La Repubblica)
- Lio singer interview (Le Monde)
- William Nordhaus, Nobel economist, dies at 85 (Le Monde)
- Northern Territory water plan condemned as attack on nature (Guardian)

**Culture / Arts:**
- How Kanye West Challenged Paul McCartney in 2014 (Vice)
- My Chemical Romance Reunite With The Used, Confirm New Album (Vice)
- Break Out the Eyeliner: My Chemical Romance reunion (Vice) - same as above

**Technology / Gaming:**
- Fortnite Pirate Shop Token how to get (Vice)
- GTA 6 fans missing work (MarketWatch) - could be Business or Gaming

**Environment:**
- Northern Territory water plan condemned (Guardian)

Now I need to merge duplicates:
- Petrol bomb/Molotov cocktail in Paris: Guardian + Le Monde (same event)
- My Chemical Romance: two Vice articles (same event)
- GTA 6: one article
- France political indecision: one article

Let me count how many stories I have after merging and proper categorization. I need 45-65 total.

Let me create the final categorized list with merged stories:

**Armed conflicts and attacks** (6-8 stories)
1. Iran's long-term strategy complicates Trump administration war planning (Bloomberg)
2. Petrol bomb thrown at French riot police in Paris; attempted murder investigation opened (Guardian, Le Monde)
3. Multiple shootings in Dallas on Halloween night leave four dead, 15 injured (Guardian)
4. One person killed in shooting outside Magic City Classic football game in Alabama (Guardian)
5. Five teenagers injured in stabbing at Halloween party in Hampshire, UK (Guardian)

**Disasters and accidents** (2-3 stories)
1. Film director Michael Mann accidentally shoots himself in leg at gun range (Guardian)
2. Cambridge scientist Marta Shahbazi dies in Spain train crash (Guardian)

**Politics and elections** (12-15 stories)
1. AI concerns move to center of US midterm campaigns (Bloomberg)
2. Traders on Kalshi and Polymarket seek election edge in Maine (Bloomberg)
3. UK urges UN Security Council members to support US resolution draft (Gov.uk)
4. Tens of thousands protest against Modi government in Delhi (Guardian)
6. Rep. DeLauro says cost of living fueling Democratic gains in midterms (Bloomberg)
7. Former NSW Liberal leads overhaul of One Nation candidate selection in Australia (Guardian)
8. Trump banks on rallies to turn out MAGA faithful ahead of midterms (Bloomberg)
9. Right-wing racism spurs South Asian political mobilization in Texas (Guardian)
10. EU officials call for end to impunity for crimes against journalists (EU Newsroom)
11. Asylum seekers still sent to France under 'one in one out' scheme weeks after it ended (Guardian)
12. Donald Tusk defends overhaul of Poland's constitutional court amid protests (Guardian)
13. German left condemns violence at protests, urges attention to demands (Le Monde)
14. French voters express indecision less than six months before 2027 presidential election (Le Monde)
15. UK Defence Secretary stockpiles food, cites need for emergency preparedness (La Repubblica)

**Law and crime** (2-3 stories)
1. Five teenagers injured in stabbing at Halloween party in Hampshire (Guardian) - already in armed conflicts? This is more crime. Let me put it in Law and crime instead.
2. Tusk defends overhaul of Poland's constitutional court (Guardian) - could be here

Actually, let me reconsider categories. Legible News might have:
- World
- Politics
- Business
- Technology
- Science & Health
- Culture
- Sports

But the user specified categories: "Armed conflicts and attacks, Disasters and accidents, Politics and elections, Law and crime, etc." So I should use those categories.

Let me finalize categories:

**Armed conflicts and attacks** (international conflicts, terrorism, war)
- Iran's Long Game Complicates Trump's War Plans (Bloomberg)
- Petrol bomb thrown at French riot police in Paris; attempted murder probe (Guardian, Le Monde)
- Multiple shootings in Dallas leave four dead, 15 injured on Halloween night (Guardian)
- Shooting outside Magic City Classic football game in Alabama kills one (Guardian)

**Disasters and accidents** (accidents, natural disasters)
- Director Michael Mann accidentally shoots himself in leg at gun range (Guardian)
- Cambridge scientist Marta Shahbazi dies in Spain train crash (Guardian)

**Politics and elections** (domestic politics, elections, government)
- AI Concerns Move to Center of Midterm Campaigns (Bloomberg)
- Traders on Kalshi/Polymarket Hunt Midterm Edge in Maine (Bloomberg)
- UK Urges UN Security Council to Support US Resolution Draft (Gov.uk)
- Tens of Thousands Protest Against Modi Government in Delhi (Guardian)
- Rep. DeLauro Sees Cost of Living Fueling Democratic Gains (Bloomberg)
- Former NSW Liberal Leads Overhaul of One Nation Candidate Selection (Guardian)
- Trump Banks on Rallies to Turn Out MAGA Faithful (Bloomberg)
- Rightwing Racism Spurs South Asian Mobilization in Texas (Guardian)
- EU Officials Call to End Impunity for Crimes Against Journalists (EU Newsroom)
- Asylum Seekers Still Sent to France Under Ended 'One In One Out' Scheme (Guardian)
- Tusk Defends Overhaul of Poland's Constitutional Court Despite Protests (Guardian)
- German Left Condemns Protest Violence, Urges Attention to Demands (Le Monde)
- French Voters Express Indecision Before 2027 Presidential Election (Le Monde)
- UK Defence Minister Stockpiles Food for Emergencies (La Repubblica)

**Law and crime** (crime, legal proceedings, law enforcement)
- Five Teenagers Hurt in Stabbing at Halloween Party in Hampshire (Guardian)
- Attempted Murder Probe After Petrol Bomb Thrown at French Police (Guardian, Le Monde) - already in armed conflicts? This is a crime investigation. Could be both but choose one.

**Business and economy** (business, finance, economy)
- Michael Dell Turned $1,000 into $302 Billion Company; Advises Founders 'Don't Go Ask' (Fortune)
- Stellantis AI Push: 'Best Thing for Career Is to Make Yourself Redundant' (Fortune)
- Binance Resumes Customer Withdrawals After Record $6.3 Billion Hack (Guardian)
- Australian Home Values Fall for Seventh Consecutive Month as Rates Dent Demand (Guardian)
- GTA 6 Release Prompts Fans to Miss Work (MarketWatch)
- Psychologist: Happiest Couples Do One Thing Differently After Time Apart (CNBC)
- Jacinda Ardern Advises Politicians to 'Rebuild Trust by Building Financial Security' (Guardian)
- At 27, Quit Dream Job Without Plan; Paid Off Over Decade Later (Business Insider)
- Airline Stopover Hack Turns Layover into Iceland Trip, Saves Money (Business Insider)

**Science and health** (science, health, medicine)
- Study: Superior Frontal Gyrus Thickness Mediates Openness and Theory of Mind (bioRxiv)
- Welsh Health Board Considers Closing Urgent Primary Care Centres at Three Hospitals (Guardian)
- South Korean Seniors Combat Loneliness with AI-Enabled Dolls (Le Monde)

**International relations** (diplomacy, global issues, regional news)
- Texas Data Center Project Divides Trump Camp (Le Monde)
- Digital Inheritance: What Happens to Data After Death (La Repubblica)
- 'Hybrid War' Label Called Euphemism for Inaction by Europeans (Le Monde)
- French Administration Confronts Antisemitic Past Through Archives and Theatre (Le Monde)
- Northern Territory Water Plan Condemned as 'Blatant Attack on Nature' (Guardian)
- William Nordhaus, Nobel Economist and Climate Pioneer, Dies at 85 (Le Monde)
- Vannacci Receives Maxi-Donations for Futuro Nazionale; Lega Gets €90k from Clinics (La Repubblica)
- François Guillemot: 'Youth Always Scares When It Moves' (Le Monde)
- Lucie's Family Secret: Fears of Sexual Abuse After Son's Birth (Le Monde)

**Culture and
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
