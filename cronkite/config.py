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
    'NewsAPI Nature': 0.95,
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