# Cronkite

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

Automated news aggregation system that collects, filters, and generates daily reports from a multitude of sources from Reuters, to r/worldnews, to University of Manchester news, and everywhere in between.

https://github.com/user-attachments/assets/6ee4bab6-bf8e-4a5a-9289-20d9037d2339.mp4

## 📰 Latest Report

**[October 27, 2026](reports/2026-10-27.md)**

*Last updated: 2026-10-27 16:26 UTC · Generated daily at 6:05 AM EST*

```
The user wants me to create a daily news report in the style of Legible News. Let me analyze the requirements:

1. Group stories by category
2. Each story as a single bullet point with headline, key details, source citations
3. Merge duplicate stories from multiple sources
4. Don't repeat stories in multiple categories
5. Clean, factual, neutral, journalistic language
6. Include hyperlinks
7. Focus on most significant/recent stories
8. Mix of sources and regions
9. 45-65 total stories
10. Start with today's date (which appears to be October 27-28, 2026 based on the articles)

Let me first organize the stories by category and identify duplicates/related stories.

Looking at the data, I see many stories from Guardian, Fortune, Vice, La Repubblica, Le Monde, etc. The categories provided in the data are:
- Business and economy
- International relations
- Politics and elections
- Armed conflicts and attacks
- Law and crime
- Disasters and accidents (not explicitly listed but Cyclone Arnab would fit)

Let me group and deduplicate:

**Armed conflicts and attacks:**
- Israel elections (multiple sources: Guardian live, Guardian article, La Repubblica, Le Monde)
- Netanyahu pressured military to attack Iran (Guardian)
- Jordan attacks militants in Syria (Guardian)
- Ukraine war updates (Le Monde live, Guardian live)
- Houthi/Egypt/Saudi tensions (Le Monde)
- US bans BYD vehicles at Japan base (Guardian)
- Melting glaciers reveal WWI munitions (Guardian)
- ABC legal action against One Nation using Bluey (Guardian)
- Brazil runoff (Guardian) - but this seems old (Oct 25)
- "First Thing: Trump targets midterm legitimacy" (Guardian)
- UK stockpiling advice / Pentagon 90 days off-grid (Fortune)
- Bottled water/tinned food sales surge (Guardian)
- "It's the smell of freedom: Belgrade cleans up after Student List triumph" (Guardian)
- Fears for Iranian athletes on death row (Guardian)
- Canceled Mass Effect 5 details leak (Vice) - this seems miscategorized
- Labour manifesto pledge accusations (Guardian)
- Fatima Payman slams PM (Guardian)
- Shabana Mahmood urged to grant visa (Guardian)

**Politics and elections:**
- Israel elections (already in armed conflicts)
- US midterms: Trump and Rubio in Texas (Guardian live)
- Trump CDC deputy director resigns (Guardian)
- UK-EU talks on free movement (Guardian)
- Guardian Essential poll: One Nation and Labor (Guardian)
- Greens push for human override in aged care (Guardian)
- Melania snub and Vatican (La Repubblica)
- UK officials discussing options with EU (Guardian)
- Brazil: Flavio Bolsonaro ordered to surrender passports (Guardian)
- EU Commission proposal on Frontex (EU Newsroom)
- Marine Le Pen ineligibility (Le Monde)
- French presidential election risk (Le Monde)
- Defender of children position vacant (Le Monde)
- Italy bus ridership record (La Repubblica)
- Palazzo Chigi seeks bank (La Repubblica)

**Law and crime:**
- Illinois man arrested for sending suspicious powder to Congress (Guardian)
- Woman's husband invited men to sexually assault her (Guardian)
- German court rejects bid to end Ukrainian ex-officer's trial over Nord Stream (ABC)
- Man serving life sentence escapes Tennessee prison (Guardian)
- Elezioni in Israele - attempted ambush at Golan (La Repubblica)
- Attentat raciste de Trappes (Le Monde)

**International relations:**
- Humans using fewer words study (Vice)
- Steam new discovery feature (Vice)
- GTA 6 Edge Magazine (Vice)
- "Juju on That Beat" rapper accuses mother (Vice)
- Beloved rock legend dies at 83 (Vice)
- Legendary rock guitarist dresses like Slipknot (Vice)
- Black Cats, Dark Metal: Rock-Star Bassist Blasko (Vice)
- 4 Signs Peter Pan Syndrome (Vice)
- India evacuates for Cyclone Arnab (ABC)
- UK stockpiling advice (Fortune/Guardian)
- Italy bus ridership (La Repubblica)
- Caterina Barbieri Venice Biennale (La Repubblica)
- Francesco De Gregori (La Repubblica)
- Jannik Sinner interview (La Repubblica)
- Colonists wanting to return to Gaza (La Repubblica)
- Pope message at Assisi (La Repubblica)
- Pirelli Calendar 2027 India (La Repubblica)
- Palazzo Chigi bank (La Repubblica)
- Oriel College event with Jason Arday accuser (Guardian)
- British politicians barred from West Bank (Guardian)
- Brazil Lula victory reader Q&A (Guardian)
- Au Brésil enquête financement étranger Flavio Bolsonaro (Le Monde)
- En Chine, propos Mbappé sur Mao (Le Monde)
- COP biodiversité subventions néfastes (Le Monde)
- L'absence prolongée Défenseur des enfants (Le Monde)
- A six mois présidentielle française (Le Monde)
- Mobilisation sociale couvre-feux (Le Monde)
- Didier Guérin on Marine Le Pen (Le Monde)
- Faac, 15 milioni dalla Curia (La Repubblica)
- US bans BYD at Japan base (Guardian) - also armed conflicts
- Nitrogen deposition forest soil (PNAS) - academic
- Altered sperm DNA methylation (PNAS) - academic
- Decoy RNA oligonucleotides (bioRxiv) - academic
- DNA damage Lamina-Associated Domains (bioRxiv) - academic
- Pretraining Knows What simulation robot (arXiv) - academic
- AI confidence study Chinese undergraduates (PLOS One) - academic
- Mitapivat sickle cell disease (Lancet) - academic
- Digital media use children (Lancet) - academic
- Pain reduction spinal injections (PLOS One) - academic
- Freddie deBoer book interview (Fortune)
- iPhone Duo foldable cracking (Fortune)
- MBA applications plunge 25% (Fortune)
- Beef imports tariffs falling short (Fortune)
- Pentagon 90 days off grid (Fortune)
- Moving to UK dream come true then left (Business Insider)
- Quit job Disney World bus driver (Business Insider)

**Business and economy:**
- Many academic papers categorized here but they're science/health
- Freddie deBoer book (Fortune)
- iPhone Duo foldable (Fortune)
- MBA applications decline (Fortune)
- Beef imports (Fortune)
- Pentagon bases 90 days off grid (Fortune)
- AI confidence study (PLOS One)
- Mitapivat sickle cell (Lancet)
- Digital media use children (Lancet)
- Pain reduction spinal injections (PLOS One)
- Nitrogen deposition (PNAS)
- Sperm DNA methylation (PNAS)
- Decoy RNA (bioRxiv)
- DNA damage (bioRxiv)
- Pretraining robot (arXiv)
- Moving to UK (Business Insider)
- Disney bus driver (Business Insider)
- Palazzo Chigi bank (La Repubblica)
- Faac 15 milioni (La Repubblica)
- Italy bus ridership (La Repubblica)
- Black Cats Dark Metal (Vice)

**Disasters and accidents:**
- India evacuates for Cyclone Arnab (ABC)
- Melting glaciers reveal munitions (Guardian) - could be here or armed conflicts

Now I need to:
1. Select the most significant stories (45-65 total)
2. Merge duplicates
3. Assign to best category
4. Write in Legible News style

Let me identify the major stories:

**Major stories to include:**
1. Israel elections - high turnout, Netanyahu vs opposition (multiple sources)
2. US midterms final week - Trump/Rubio in Texas, lawsuits, cash bounty (Guardian)
3. Ukraine war - Swedish PM on peace terms, Russian attacks on energy (Le Monde)
4. Jordan strikes Syria militants after church attack (Guardian)
5. Houthi threat over Egypt-Saudi military cooperation (Le Monde)
6. UK emergency stockpiling advice - Pentagon 90-day grid-down planning, UK govt advice, panic buying (Fortune, Guardian)
7. Cyclone Arnab - India evacuates tens of thousands (ABC)
8. German court - Ukrainian ex-officer Nord Stream trial continues (ABC)
9. Illinois man arrested sending powder to Congress (Guardian)
10. Tennessee prison escape - life sentence murderer (Guardian)
11. UK-EU talks on free movement ahead of summit (Guardian)
12. Trump CDC deputy director resigns after 6 months (Guardian)
13. Labour accused of breaking manifesto pledge on youth minimum wage (Guardian)
14. Guardian Essential poll - One Nation equals Labor primary vote (Guardian)
15. Greens push human override in aged care after algorithm report (Guardian)
16. Fatima Payman slams PM over MP safety (Guardian)
17. French presidential election 6 months out - fear/exasperation/authority demand (Le Monde)
18. Marine Le Pen currently ineligible per magistrate (Le Monde)
19. Defender of children position vacant - associations pressure govt (Le Monde)
20. COP biodiversity - harmful subsidies central to negotiations (Le Monde)
21. Brazil - Flavio Bolsonaro ordered to surrender passports (Guardian)
22. Brazil - investigation into possible foreign financing of Flavio Bolsonaro campaign (Le Monde)
23. US bans BYD vehicles at Japan military base (Guardian)
24. British politicians barred from West Bank (Guardian)
25. iPhone Duo foldable screens cracking within hours (Fortune)
26. MBA applications plunge 25% as Gen Z questions value (Fortune)
27. Trump beef imports promise - shipments lag, prices unchanged (Fortune)
28. Humans using significantly fewer words than 20 years ago (Vice)
29. Pope at Assisi: "No holy war, only peace is holy" (La Repubblica)
30. Melting glaciers in Dolomites reveal WWI munitions (Guardian)
31. Belgrade cleans up after Student List triumph (Guardian)
32. Iranian athletes on death row fears - mountaineer hanged (Guardian)
33. Steam rolls out major new discovery feature (Vice)
34. GTA 6 Edge Magazine release details (Vice)
35. "Juju on That Beat" rapper accuses mother of taking $17M (Vice)
36. Rock legend dies at 83 after final performance (Vice)
37. Italy bus ridership record (La Repubblica)
38. Caterina Barbieri: Venice Biennale must remain sanctuary for artistic freedom (La Repubblica)
39. UK officials discussing options including free movement with EU (Guardian) - duplicate of 11
40. Netanyahu reportedly pressured military to attack Iran before election (Guardian)
41. ABC legal action against One Nation for using Bluey (Guardian)
42. Woman's world tilted - husband invited men to assault her (Guardian)
43. Trappes racist attack - Lecornu denounces discourse that arms others (Le Monde)
44. Administrative courts battle against state-decreed curfews (Le Monde)
45. Mbappé comments on Mao in China have exorbitant financial cost (Le Monde)
46. Oriel College urged to cancel event with Jason Arday accuser (Guardian)
47. Shabana Mahmood urged to grant visa to former Weather Underground activist (Guardian)
48. Melania snub and Vatican tensions (La Repubblica)
49. Pretraining Knows What, Simulation Teaches How - robot agent (arXiv)
50. Mitapivat phase 3 trial for sickle cell disease (Lancet)
51. Digital media use children's health framework (Lancet)
52. Nitrogen deposition doesn't alter forest soil carbon (PNAS)
53. Altered sperm DNA methylation intergenerational disease (PNAS)
54. Moving to UK felt like dream, 5 years later left (Business Insider)
55. Quit job at 44 to be Disney World bus driver (Business Insider)
56. Freddie deBoer new book on psychiatry/disability (Fortune)
57. Palazzo Chigi seeks bank for employees, €1M contract (La Repubblica)
58. Faac, 15M from Curia for charity, Zuppi refuses company funds (La Repubblica)
59. Francesco De Gregori rehearsals (La Repubblica)
60. Jannik Sinner interview (La Repubblica)
61. Colonists waiting to return to Gaza (La Repubblica)
62. Pirelli Calendar 2027 explores India (La Repubblica)
63. Black Cats Dark Metal - bassist Blasko cat advocacy (Vice)
64. 4 Signs Peter Pan Syndrome (Vice)
65. Legendary rock guitarist dresses as Slipknot member (Vice)
66. Canceled Mass Effect 5 details leak (Vice)
67. Reader Q&A on Lula Brazil victory (Guardian)
68. How Lula beat Bolsonaro audio (Guardian)
69. Brazil runoff as it happened (Guardian) - older
70. First Thing: Trump targets midterm legitimacy (Guardian)
71. EN DIRECT Israel legislatives - participation record (Le Monde)
72. EN DIRECT Ukraine war (Le Monde)
73. Au Yemen Houthi assimilent soutien égyptien à déclaration de guerre (Le Monde)
74. Au Brésil enquête financement étranger Flavio Bolsonaro (Le Monde)
75. En Chine propos Mbappé sur Mao (Le Monde)
76. COP biodiversité subventions néfastes (Le Monde)
77. A six mois présidentielle française (Le Monde)
78. L'absence prolongée Défenseur des enfants (Le Monde)
79. Mobilisation sociale couvre-feux (Le Monde)
80. Didier Guérin Marine Le Pen inéligible (Le Monde)
81. Attentat raciste Trappes (Le Monde)
82. Elezioni Israele news affluenza record (La Repubblica)
83. Palazzo Chigi cerca banca (La Repubblica)
84. Caterina Barbieri Venezia Biennale (La Repubblica)
85. Francesco De Gregori prove (La Repubblica)
86. Jannik Sinner intervista (La Repubblica)
87. Tra i coloni Gaza (La Repubblica)
88. Papa Assisi messaggio pace (La Repubblica)
89. Pirelli Calendar 2027 India (La Repubblica)
90. Faac 15 milioni Curia (La Repubblica)
91. US bans BYD at Kadena (Guardian)
92. British politicians barred West Bank (Guardian)
93. Jordan attacks Syria (Guardian)
94. Melting glaciers Dolomites (Guardian)
95. Belgrade Student List (Guardian)
96. Iranian athletes death row (Guardian)
97. ABC One Nation Bluey (Guardian)
98. Woman husband assault (Guardian)
99. Illinois man powder Congress (Guardian)
100. Tennessee prison escape (Guardian)
101. German court Nord Stream (ABC)
102. Cyclone Arnab India (ABC)
103. UK stockpiling advice (Fortune, Guardian)
104. Pentagon 90 days off grid (Fortune)
105. iPhone Duo cracking (Fortune)
106. MBA applications plunge (Fortune)
107. Beef imports tariffs (Fortune)
108. Freddie deBoer book (Fortune)
109. Moving to UK dream (Business Insider)
110. Disney bus driver (Business Insider)
111. Humans fewer words (Vice)
112. Steam discovery feature (Vice)
113. GTA 6 Edge (Vice)
114. Juju on That Beat rapper (Vice)
115. Rock legend dies 83 (Vice)
116. Rock guitarist Slipknot (Vice)
117. Black Cats Dark Metal (Vice)
118. Peter Pan Syndrome (Vice)
119. Canceled Mass Effect 5 (Vice)
120. Italy bus record (La Repubblica)
112. Pretraining robot (arXiv)
113. AI confidence study (PLOS One)
114. Mitapivat sickle cell (Lancet)
115. Digital media children (Lancet)
116. Pain reduction spinal (PLOS One)
117. Nitrogen deposition (PNAS)
118. Sperm DNA methylation (PNAS)
119. Decoy RNA (bioRxiv)
120. DNA damage Lamina (bioRxiv)

That's way too many. I need to select ~50-60 most significant, merging duplicates.

Let me create the final list organized by category, selecting the most newsworthy:

**Armed conflicts and attacks (10-12 stories)**
1. Israel legislative elections - record turnout, Netanyahu vs opposition
2. Netanyahu reportedly pressured military to attack Iran before election
3. Ukraine war - Swedish PM: peace must be on Kyiv's terms; Russian strikes on energy infrastructure
4. Jordan strikes militants in Syria retaliating for church attack
5. Houthis equate Egyptian military support for Saudi Arabia to declaration of war
6. UK emergency preparedness: Pentagon plans 90 days off-grid; UK govt advises stockpiling; panic buying of water/tinned food
7. US bans BYD electric vehicles from Kadena military base in Japan
8. Melting glaciers in Dolomites reveal WWI munitions cache
9. Belgrade cleanup after Student List election triumph
10. Fears for Iranian athletes on death row after mountaineer execution
11. ABC to take legal action against One Nation for using Bluey in cartoon
12. Trappes racist attack: French minister denounces rhetoric that arms perpetrators

**Politics and elections (10-12 stories)**
1. US midterms final week: Trump and Rubio campaign in Texas; Trump files lawsuits and offers cash bounty challenging legitimacy
2. Trump-appointed CDC deputy director Jennifer Shuford resigns after six months
3. UK
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
