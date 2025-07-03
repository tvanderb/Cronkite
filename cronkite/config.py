SOURCE_WEIGHTS = {
    'BBC World': 1.0,
    'Guardian World': 0.9,
    'Reuters World': 0.95,
    'CNN World': 0.85,
    'ABC News': 0.8,
    'NPR World': 0.9,
    'Al Jazeera': 0.85,
    # International sources
    'Le Monde': 0.9,
    'Der Spiegel': 0.9,
    'El País': 0.85,
    'La Repubblica': 0.8,
    'Asahi Shimbun': 0.85,
    'South China Morning Post': 0.8,
    # Specialized sources
    'The Economist': 0.9,
    'Financial Times': 0.9,
    'Nature': 0.95,
    'Science': 0.95,
    'The Atlantic': 0.8,
    'New Yorker': 0.8,
    # Regional/Alternative sources
    'Associated Press': 0.95,
    'Agence France-Presse': 0.9,
    'Bloomberg': 0.85,
    'Vice News': 0.6,
    'Vox': 0.7,
    'Politico': 0.8,
    # NewsAPI sources (common sources that may appear)
    'NewsAPI Reuters': 0.95,
    'NewsAPI Associated Press': 0.95,
    'NewsAPI BBC News': 1.0,
    'NewsAPI CNN': 0.85,
    'NewsAPI The New York Times': 0.9,
    'NewsAPI The Washington Post': 0.9,
    'NewsAPI NPR': 0.9,
    'NewsAPI USA Today': 0.8,
    'NewsAPI Los Angeles Times': 0.8,
    'NewsAPI The Wall Street Journal': 0.9,
    'NewsAPI Bloomberg': 0.85,
    'NewsAPI Politico': 0.8,
    'NewsAPI The Atlantic': 0.8,
    'NewsAPI The Economist': 0.9,
    'NewsAPI Financial Times': 0.9,
    'NewsAPI Science': 0.95,
    # Social media sources
    'Reddit r/news': 0.7,
    'Reddit r/worldnews': 0.7,
    'Reddit r/inthenews': 0.6,
    'Reddit r/politics': 0.6,
    'Reddit r/worldpolitics': 0.6,
    'Reddit r/europe': 0.5,
    'Reddit r/uknews': 0.5,
    'Reddit r/usanews': 0.5,
    'Reddit r/science': 0.6,
    'Reddit r/technology': 0.6,
    'Reddit r/environment': 0.5,
    'Reddit r/business': 0.6,
    'Hacker News': 0.6,
    'Mastodon (mastodon.social)': 0.5,
}

# High-reliability sources for cross-verification
HIGH_RELIABILITY_SOURCES = {
    'Reuters World', 'BBC World', 'Guardian World', 'NPR World', 
    'Al Jazeera', 'CNN World', 'ABC News', 'Associated Press',
    'Agence France-Presse', 'Le Monde', 'Der Spiegel', 'Nature',
    'Science', 'The Economist', 'Financial Times'
}

# Source hierarchy for deduplication (higher = more preferred)
SOURCE_HIERARCHY = {
    'Reuters World': 10,
    'Associated Press': 10,
    'Nature': 10,
    'Science': 10,
    'BBC World': 9,
    'Guardian World': 8,
    'NPR World': 8,
    'Le Monde': 8,
    'Der Spiegel': 8,
    'The Economist': 8,
    'Financial Times': 8,
    'Agence France-Presse': 8,
    'Al Jazeera': 7,
    'CNN World': 7,
    'El País': 7,
    'Asahi Shimbun': 7,
    'ABC News': 6,
    'Bloomberg': 6,
    'Politico': 6,
    'La Repubblica': 6,
    'South China Morning Post': 6,
    'The Atlantic': 5,
    'New Yorker': 5,
    'Hacker News': 5,
    'Vox': 4,
    'Reddit r/news': 4,
    'Reddit r/worldnews': 4,
    'Reddit r/science': 4,
    'Reddit r/technology': 4,
    'Reddit r/business': 4,
    'Reddit r/politics': 3,
    'Reddit r/worldpolitics': 3,
    'Reddit r/inthenews': 3,
    'Reddit r/europe': 2,
    'Reddit r/uknews': 2,
    'Reddit r/usanews': 2,
    'Reddit r/environment': 2,
    'Vice News': 2,
    'Mastodon (mastodon.social)': 1,
}

# Keywords that indicate opinion pieces or subjective content
OPINION_KEYWORDS = [
    'opinion', 'comment', 'analysis', 'view', 'perspective', 'column',
    'shaky', 'genie', 'comeback', 'climbdown', 'capitalize',
    'what happens next', 'lets', 'no one knows', 'could', 'might', 'may',
    'should', 'would', 'think', 'believe', 'feel', 'seem', 'appear',
    'suggests', 'indicates', 'implies', 'argues', 'claims', 'says',
    'editorial', 'op-ed', 'commentary', 'viewpoint', 'take', 'stance'
]

# URL patterns that indicate opinion content
OPINION_URL_PATTERNS = [
    '/opinion/', '/comment/', '/analysis/', '/view/', '/perspective/',
    '/column/', '/editorial/', '/op-ed/', '/commentary/', '/viewpoint/',
    '/blog/', '/blogs/', '/opinions/', '/commentary/', '/analysis/',
    'opinion.', 'comment.', 'analysis.', 'view.', 'perspective.'
]

# Reddit flairs that indicate opinion content
OPINION_REDDIT_FLAIRS = [
    'opinion', 'editorial', 'analysis', 'commentary', 'viewpoint',
    'perspective', 'column', 'op-ed', 'comment', 'analysis'
]

# Known unreliable or fake news sources (to be filtered out)
UNRELIABLE_SOURCES = {
    'infowars.com', 'breitbart.com', 'thegatewaypundit.com', 'naturalnews.com',
    'worldnetdaily.com', 'prisonplanet.com', 'beforeitsnews.com', 'veteranstoday.com',
    'yournewswire.com', 'endingthefed.com', 'activistpost.com', 'collective-evolution.com'
}

# Domain reputation scores (higher = more reliable)
DOMAIN_REPUTATION = {
    # Major news outlets
    'reuters.com': 0.95, 'bbc.com': 1.0, 'theguardian.com': 0.9, 'cnn.com': 0.85,
    'nytimes.com': 0.9, 'washingtonpost.com': 0.9, 'wsj.com': 0.9, 'npr.org': 0.9,
    'ap.org': 0.95, 'afp.com': 0.9, 'bloomberg.com': 0.85, 'politico.com': 0.8,
    'economist.com': 0.9, 'ft.com': 0.9, 'nature.com': 0.95, 'science.org': 0.95,
    'lemonde.fr': 0.9, 'spiegel.de': 0.9, 'elpais.com': 0.85, 'repubblica.it': 0.8,
    'asahi.com': 0.85, 'scmp.com': 0.8, 'theatlantic.com': 0.8, 'newyorker.com': 0.8,
    'vice.com': 0.6, 'vox.com': 0.7,
    
    # US Government sources
    'whitehouse.gov': 0.95, 'state.gov': 0.95, 'congress.gov': 0.95,
    'defense.gov': 0.95, 'energy.gov': 0.95, 'justice.gov': 0.95, 'dhs.gov': 0.95,
    'hhs.gov': 0.95, 'transportation.gov': 0.95, 'ed.gov': 0.95, 'commerce.gov': 0.95,
    'usda.gov': 0.95, 'dol.gov': 0.95, 'va.gov': 0.95, 'doi.gov': 0.95,
    'treasury.gov': 0.95, 'epa.gov': 0.95, 'fbi.gov': 0.95, 'cia.gov': 0.95,
    'nsa.gov': 0.95, 'nasa.gov': 0.95, 'nih.gov': 0.95, 'cdc.gov': 0.95, 'fda.gov': 0.95,
    'house.gov': 0.95, 'senate.gov': 0.95, 'supremecourt.gov': 0.95,
    
    # Canadian Government sources
    'canada.ca': 0.95, 'pm.gc.ca': 0.95, 'international.gc.ca': 0.95,
    'publicsafety.gc.ca': 0.95, 'tc.gc.ca': 0.95, 'ic.gc.ca': 0.95,
    
    # US Universities
    'harvard.edu': 0.9, 'mit.edu': 0.9, 'stanford.edu': 0.9, 'berkeley.edu': 0.9,
    'yale.edu': 0.9, 'princeton.edu': 0.9, 'columbia.edu': 0.9, 'uchicago.edu': 0.9,
    'caltech.edu': 0.9, 'jhu.edu': 0.9, 'upenn.edu': 0.9, 'duke.edu': 0.9,
    'northwestern.edu': 0.9, 'umich.edu': 0.9, 'ucla.edu': 0.9, 'ucsd.edu': 0.9,
    'cmu.edu': 0.9, 'cornell.edu': 0.9, 'washington.edu': 0.9, 'utexas.edu': 0.9,
    
    # UK Universities
    'ox.ac.uk': 0.9, 'cam.ac.uk': 0.9, 'imperial.ac.uk': 0.9, 'ucl.ac.uk': 0.9,
    'lse.ac.uk': 0.9, 'kcl.ac.uk': 0.9, 'ed.ac.uk': 0.9, 'manchester.ac.uk': 0.9,
    'bristol.ac.uk': 0.9,
    
    # Canadian Universities
    'utoronto.ca': 0.9, 'ubc.ca': 0.9, 'mcgill.ca': 0.9, 'ualberta.ca': 0.9,
    'uwaterloo.ca': 0.9, 'umontreal.ca': 0.9,
    
    # International Universities
    'ethz.ch': 0.9, 'u-tokyo.ac.jp': 0.9, 'nus.edu.sg': 0.9, 'unimelb.edu.au': 0.9,
    'sydney.edu.au': 0.9, 'pku.edu.cn': 0.9, 'tsinghua.edu.cn': 0.9,
    
    # Research Institutions and Journals
    'nature.com': 0.95, 'science.org': 0.95, 'cell.com': 0.9, 'thelancet.com': 0.9,
    'nejm.org': 0.9, 'jamanetwork.com': 0.9, 'pnas.org': 0.95, 'plos.org': 0.85,
    'arxiv.org': 0.8, 'biorxiv.org': 0.8,
    
    # Industry sources
    'techcrunch.com': 0.7, 'wired.com': 0.8, 'ars-technica.com': 0.8,
    'theverge.com': 0.7, 'engadget.com': 0.7, 'gizmodo.com': 0.6,
    'forbes.com': 0.8, 'fortune.com': 0.8, 'businessinsider.com': 0.7,
    'cnbc.com': 0.8, 'marketwatch.com': 0.8, 'yahoo.com': 0.7,
}

# Content quality thresholds
CONTENT_QUALITY_THRESHOLDS = {
    'min_title_length': 10,
    'max_title_length': 200,
    'min_summary_length': 20,
    'max_summary_length': 500,
    'min_word_count': 50,
    'max_word_count': 2000,
}

# Geographic diversity targets (minimum stories per region)
GEOGRAPHIC_DIVERSITY = {
    'north_america': 0.3,  # 30% of stories
    'europe': 0.25,        # 25% of stories
    'asia': 0.2,           # 20% of stories
    'other': 0.25,         # 25% of stories
}

# Government RSS feeds
GOVERNMENT_RSS_FEEDS = [
    # US Federal Government
    ('White House', 'https://www.whitehouse.gov/feed/'),
    ('State Department', 'https://www.state.gov/feed/'),
    ('Department of Defense', 'https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=944&max=20'),
    ('Department of Energy', 'https://www.energy.gov/feeds/energygov-news'),
    ('Department of Justice', 'https://www.justice.gov/feeds/justice-news'),
    ('Department of Homeland Security', 'https://www.dhs.gov/feeds/news'),
    ('Department of Health and Human Services', 'https://www.hhs.gov/feeds/news'),
    ('Department of Transportation', 'https://www.transportation.gov/feeds/news'),
    ('Department of Education', 'https://www.ed.gov/feeds/news'),
    ('Department of Commerce', 'https://www.commerce.gov/feeds/news'),
    ('Department of Agriculture', 'https://www.usda.gov/feeds/news'),
    ('Department of Labor', 'https://www.dol.gov/feeds/news'),
    ('Department of Veterans Affairs', 'https://www.va.gov/feeds/news'),
    ('Department of Interior', 'https://www.doi.gov/feeds/news'),
    ('Department of Treasury', 'https://home.treasury.gov/feeds/news'),
    ('Environmental Protection Agency', 'https://www.epa.gov/feeds/news'),
    ('Federal Bureau of Investigation', 'https://www.fbi.gov/feeds/news'),
    ('Central Intelligence Agency', 'https://www.cia.gov/feeds/news'),
    ('National Security Agency', 'https://www.nsa.gov/feeds/news'),
    ('NASA', 'https://www.nasa.gov/feed/'),
    ('NIH News', 'https://www.nih.gov/news-events/news-releases/rss.xml'),
    ('CDC News', 'https://tools.cdc.gov/api/v2/resources/media/132404.rss'),
    ('FDA News', 'https://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/rss.xml'),
    ('Congress House', 'https://www.house.gov/feeds/rss/news'),
    ('Congress Senate', 'https://www.senate.gov/feeds/rss/news'),
    ('Supreme Court', 'https://www.supremecourt.gov/feeds/news'),
    # Canadian Government
    ('Government of Canada', 'https://www.canada.ca/en/news/feed.xml'),
    ('Prime Minister of Canada', 'https://pm.gc.ca/en/news/feed'),
    ('Global Affairs Canada', 'https://www.international.gc.ca/world-monde/news-news/index.aspx?view=rss'),
    ('Department of National Defence Canada', 'https://www.canada.ca/en/department-national-defence/news/feed.xml'),
    ('Health Canada', 'https://www.canada.ca/en/health-canada/news/feed.xml'),
    ('Environment and Climate Change Canada', 'https://www.canada.ca/en/environment-climate-change/news/feed.xml'),
    ('Public Safety Canada', 'https://www.publicsafety.gc.ca/cnt/ntnl-scrt/cntr-trrrsm/feed.xml'),
    ('Transport Canada', 'https://www.tc.gc.ca/en/news/feed.xml'),
    ('Innovation, Science and Economic Development Canada', 'https://www.ic.gc.ca/eic/site/icgc.nsf/eng/feed.xml'),
]

# Remove Chinese sources from GOVERNMENT_RSS_FEEDS
GOVERNMENT_RSS_FEEDS = [
    s for s in GOVERNMENT_RSS_FEEDS
    if not (
        'china' in s[0].lower() or
        'chinese' in s[0].lower() or
        '.cn' in s[1] or
        'scmp.com' in s[1] or
        'asahi.com' in s[1]
    )
]

# Academic RSS feeds
ACADEMIC_RSS_FEEDS = [
    # US Universities
    ('Harvard Gazette', 'https://news.harvard.edu/gazette/feed/'),
    ('MIT News', 'https://news.mit.edu/rss/feed'),
    ('Stanford News', 'https://news.stanford.edu/feed/'),
    ('UC Berkeley News', 'https://news.berkeley.edu/feed/'),
    ('Yale News', 'https://news.yale.edu/feed'),
    ('Princeton News', 'https://www.princeton.edu/news/feed'),
    ('Columbia News', 'https://news.columbia.edu/feed'),
    ('University of Chicago News', 'https://news.uchicago.edu/feed'),
    ('Caltech News', 'https://www.caltech.edu/about/news/feed'),
    ('Johns Hopkins News', 'https://hub.jhu.edu/feed/'),
    ('University of Pennsylvania News', 'https://penntoday.upenn.edu/feed'),
    ('Duke News', 'https://today.duke.edu/feed'),
    ('Northwestern News', 'https://news.northwestern.edu/feed/'),
    ('University of Michigan News', 'https://news.umich.edu/feed/'),
    ('UC Los Angeles News', 'https://newsroom.ucla.edu/feed'),
    ('UC San Diego News', 'https://ucsdnews.ucsd.edu/feed'),
    ('Carnegie Mellon News', 'https://www.cmu.edu/news/feed/'),
    ('Cornell News', 'https://news.cornell.edu/feed'),
    ('University of Washington News', 'https://www.washington.edu/news/feed/'),
    ('University of Texas News', 'https://news.utexas.edu/feed/'),
    # UK Universities
    ('Oxford News', 'https://www.ox.ac.uk/news-and-events/rss'),
    ('Cambridge News', 'https://www.cam.ac.uk/news/feed'),
    ('Imperial College London News', 'https://www.imperial.ac.uk/news/feed/'),
    ('University College London News', 'https://www.ucl.ac.uk/news/feed'),
    ('London School of Economics News', 'https://www.lse.ac.uk/News/feed'),
    ('King\'s College London News', 'https://www.kcl.ac.uk/news/feed'),
    ('University of Edinburgh News', 'https://www.ed.ac.uk/news/feed'),
    ('University of Manchester News', 'https://www.manchester.ac.uk/discover/news/feed/'),
    ('University of Bristol News', 'https://www.bristol.ac.uk/news/feed/'),
    # Canadian Universities
    ('University of Toronto News', 'https://www.utoronto.ca/news/feed'),
    ('University of British Columbia News', 'https://news.ubc.ca/feed/'),
    ('McGill University News', 'https://www.mcgill.ca/newsroom/feed'),
    ('University of Alberta News', 'https://www.ualberta.ca/news/feed'),
    ('University of Waterloo News', 'https://uwaterloo.ca/news/feed'),
    ('University of Montreal News', 'https://nouvelles.umontreal.ca/en/feed/'),
    # International Universities
    ('ETH Zurich News', 'https://ethz.ch/en/news-and-events/eth-news.html/rss'),
    ('University of Tokyo News', 'https://www.u-tokyo.ac.jp/en/news/feed'),
    ('National University of Singapore News', 'https://news.nus.edu.sg/feed/'),
    ('University of Melbourne News', 'https://newsroom.unimelb.edu.au/feed'),
    ('University of Sydney News', 'https://www.sydney.edu.au/news/feed'),
    ('Peking University News', 'https://english.pku.edu.cn/news_events/news/feed'),
    ('Tsinghua University News', 'https://www.tsinghua.edu.cn/en/news/feed'),
    # Research Institutions and Journals
    ('Nature News', 'https://www.nature.com/nature.rss'),
    ('Science News', 'https://www.science.org/rss/news_current.xml'),
    ('Cell Press', 'https://www.cell.com/rss/current.xml'),
    ('The Lancet', 'https://www.thelancet.com/rssfeed/lancet_current.xml'),
    ('New England Journal of Medicine', 'https://www.nejm.org/feed/rss/recent'),
    ('JAMA Network', 'https://jamanetwork.com/rss/site_3/67/feed.xml'),
    ('Proceedings of the National Academy of Sciences', 'https://www.pnas.org/rss/current.xml'),
    ('PLOS One', 'https://journals.plos.org/plosone/feed/atom'),
    ('arXiv', 'http://export.arxiv.org/rss/cs.AI'),
    ('bioRxiv', 'https://connect.biorxiv.org/biorxiv_xml.php?subject=all'),
]

# Remove Chinese sources from ACADEMIC_RSS_FEEDS
ACADEMIC_RSS_FEEDS = [
    s for s in ACADEMIC_RSS_FEEDS
    if not (
        'china' in s[0].lower() or
        'chinese' in s[0].lower() or
        '.cn' in s[1] or
        'peking' in s[0].lower() or
        'tsinghua' in s[0].lower()
    )
]

# Remove Chinese sources from DOMAIN_REPUTATION
DOMAIN_REPUTATION = {
    k: v for k, v in DOMAIN_REPUTATION.items()
    if not (
        k.endswith('.cn') or
        'scmp.com' in k or
        'asahi.com' in k or
        'peking' in k or
        'tsinghua' in k
    )
}

# Industry RSS feeds
INDUSTRY_RSS_FEEDS = [
    ('TechCrunch', 'https://techcrunch.com/feed/'),
    ('Wired', 'https://www.wired.com/feed/rss'),
    ('Ars Technica', 'https://feeds.arstechnica.com/arstechnica/index'),
    ('The Verge', 'https://www.theverge.com/rss/index.xml'),
    ('Engadget', 'https://www.engadget.com/rss.xml'),
    ('Forbes Tech', 'https://www.forbes.com/technology/feed/'),
    ('Fortune', 'https://fortune.com/feed/'),
    ('Business Insider', 'https://www.businessinsider.com/rss'),
    ('CNBC', 'https://www.cnbc.com/id/100003114/device/rss/rss.html'),
    ('MarketWatch', 'https://feeds.marketwatch.com/marketwatch/topstories/'),
] 