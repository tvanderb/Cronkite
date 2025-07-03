SOURCE_WEIGHTS = {
    'BBC World': 1.0,
    'Guardian World': 0.9,
    'Reuters World': 0.95,
    'CNN World': 0.85,
    'ABC News': 0.8,
    'NPR World': 0.9,
    'Al Jazeera': 0.85,
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