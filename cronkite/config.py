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
    'South China Morning Post': 0.4,
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
    # Government sources
    'NASA': 8,
    'Government of Canada': 8,
    'Supreme Court of Canada': 8,
    'Canadian Centre for Cyber Security': 8,
    'White House (USA)': 8,
    'CDC Newsroom (USA)': 8,
    'FEMA News (USA)': 8,
    'GOV.UK News (UK)': 8,
    'UK Parliament': 8,
    'Australian Government News': 8,
    'Australian Department of Health': 8,
    'EU Newsroom': 8,
    'Beehive (NZ Government)': 8,
    'United Nations News': 8,
    # Academic sources
    'Harvard Gazette': 0.9,
    'MIT News': 0.9,
    'UC Berkeley News': 0.9,
    'University of Michigan News': 0.9,
    'Johns Hopkins News': 0.9,
    'University of Washington News': 0.9,
    'University of British Columbia News': 0.9,
    'University of Manchester News': 0.9,
    'Nature News': 0.95,
    'Science News': 0.95,
    'The Lancet': 0.9,
    'Proceedings of the National Academy of Sciences': 0.95,
    'PLOS One': 0.85,
    'arXiv': 0.8,
    'bioRxiv': 0.8,
    # Industry sources
    'TechCrunch': 0.7,
    'Wired': 0.8,
    'Ars Technica': 0.8,
    'The Verge': 0.7,
    'Engadget': 0.7,
    'Forbes Tech': 0.8,
    'Fortune': 0.8,
    'Business Insider': 0.7,
    'CNBC': 0.8,
    'MarketWatch': 0.8,
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
    # Academic sources
    'Harvard Gazette': 7,
    'MIT News': 7,
    'UC Berkeley News': 7,
    'University of Michigan News': 7,
    'Johns Hopkins News': 7,
    'University of Washington News': 7,
    'University of British Columbia News': 7,
    'University of Manchester News': 7,
    'Nature News': 9,
    'Science News': 9,
    'The Lancet': 8,
    'Proceedings of the National Academy of Sciences': 9,
    'PLOS One': 7,
    'arXiv': 6,
    'bioRxiv': 6,
    # Industry sources
    'TechCrunch': 6,
    'Wired': 6,
    'Ars Technica': 6,
    'The Verge': 6,
    'Engadget': 6,
    'Forbes Tech': 6,
    'Fortune': 6,
    'Business Insider': 6,
    'CNBC': 6,
    'MarketWatch': 6,
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

# Domain reputation scores (higher = more reliable) - only working sources
DOMAIN_REPUTATION = {
    # Major news outlets - working feeds
    'reuters.com': 0.95, 'bbc.com': 1.0, 'theguardian.com': 0.9, 'cnn.com': 0.85,
    'nytimes.com': 0.9, 'washingtonpost.com': 0.9, 'wsj.com': 0.9, 'npr.org': 0.9,
    'ap.org': 0.95, 'afp.com': 0.9, 'bloomberg.com': 0.85, 'politico.com': 0.8,
    'economist.com': 0.9, 'ft.com': 0.9, 'nature.com': 0.95, 'science.org': 0.95,
    'lemonde.fr': 0.9, 'spiegel.de': 0.9, 'elpais.com': 0.85, 'repubblica.it': 0.8,
    'asahi.com': 0.85, 'scmp.com': 0.8, 'theatlantic.com': 0.8, 'newyorker.com': 0.8,
    'vice.com': 0.6, 'vox.com': 0.7,
    
    # US Government sources - working feeds only
    'nasa.gov': 0.95,
    'whitehouse.gov': 0.95,
    'cdc.gov': 0.95,
    'fema.gov': 0.95,
    
    # Canadian Government sources - working feeds only
    'canada.ca': 0.95,
    'scc-csc.ca': 0.95,
    'cyber.gc.ca': 0.95,
    
    # UK Government
    'gov.uk': 0.95,
    'parliament.uk': 0.95,
    
    # Australian Government
    'australia.gov.au': 0.95,
    'health.gov.au': 0.95,
    
    # EU
    'europa.eu': 0.95,
    
    # New Zealand
    'beehive.govt.nz': 0.95,
    
    # United Nations
    'un.org': 0.95,
    
    # US Universities - working feeds only
    'harvard.edu': 0.9, 'mit.edu': 0.9, 'berkeley.edu': 0.9,
    'umich.edu': 0.9, 'jhu.edu': 0.9, 'washington.edu': 0.9, 'ubc.ca': 0.9,
    'manchester.ac.uk': 0.9,
    
    # Research Institutions and Journals - working feeds only
    'nature.com': 0.95, 'science.org': 0.95, 'thelancet.com': 0.9,
    'pnas.org': 0.95, 'plos.org': 0.85, 'arxiv.org': 0.8, 'biorxiv.org': 0.8,
    
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

# Main RSS feeds - only working ones
RSS_FEEDS = [
    # Major international news sources
    ('BBC World', 'https://feeds.bbci.co.uk/news/world/rss.xml'),
    ('Guardian World', 'https://www.theguardian.com/world/rss'),
    ('CNN World', 'http://rss.cnn.com/rss/edition.rss'),
    ('ABC News', 'https://abcnews.go.com/abcnews/internationalheadlines'),
    ('NPR World', 'https://feeds.npr.org/1004/rss.xml'),
    ('Al Jazeera', 'https://www.aljazeera.com/xml/rss/all.xml'),
    ('Le Monde', 'https://www.lemonde.fr/rss/une.xml'),
    ('La Repubblica', 'https://www.repubblica.it/rss/homepage/rss2.0.xml'),
    ('The Economist', 'https://www.economist.com/international/rss.xml'),
    ('Financial Times', 'https://www.ft.com/world?format=rss'),
    ('Nature', 'https://www.nature.com/nature.rss'),
    ('Science', 'https://www.science.org/rss/news_current.xml'),
    ('The Atlantic', 'https://www.theatlantic.com/feed/all/'),
    ('New Yorker', 'https://www.newyorker.com/feed/everything'),
    ('Bloomberg', 'https://feeds.bloomberg.com/politics/news.rss'),
    ('Vice News', 'https://www.vice.com/en/rss'),
    ('Vox', 'https://www.vox.com/rss/index.xml'),
]

# Government RSS feeds - only working ones
GOVERNMENT_RSS_FEEDS = [
    # US Federal Government - only working feeds
    ('NASA', 'https://www.nasa.gov/feed/'),
    # Canadian Government - only working feeds
    ('Government of Canada', 'https://www.canada.ca/en/news/feed.xml'),
]

# Academic RSS feeds - only working ones
ACADEMIC_RSS_FEEDS = [
    # US Universities - only working feeds
    ('Harvard Gazette', 'https://news.harvard.edu/gazette/feed/'),
    ('MIT News', 'https://news.mit.edu/rss/feed'),
    ('UC Berkeley News', 'https://news.berkeley.edu/feed/'),
    ('University of Michigan News', 'https://news.umich.edu/feed/'),
    ('Johns Hopkins News', 'https://hub.jhu.edu/feed/'),
    ('University of Washington News', 'https://www.washington.edu/news/feed/'),
    ('University of British Columbia News', 'https://news.ubc.ca/feed/'),
    ('University of Manchester News', 'https://www.manchester.ac.uk/discover/news/feed/'),
    # Research Institutions and Journals - only working feeds
    ('Nature News', 'https://www.nature.com/nature.rss'),
    ('Science News', 'https://www.science.org/rss/news_current.xml'),
    ('The Lancet', 'https://www.thelancet.com/rssfeed/lancet_current.xml'),
    ('Proceedings of the National Academy of Sciences', 'https://www.pnas.org/rss/current.xml'),
    ('PLOS One', 'https://journals.plos.org/plosone/feed/atom'),
    ('arXiv', 'http://export.arxiv.org/rss/cs.AI'),
    ('bioRxiv', 'https://connect.biorxiv.org/biorxiv_xml.php?subject=all'),
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
