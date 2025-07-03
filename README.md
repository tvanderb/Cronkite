# Cronkite - Advanced News Aggregator

A sophisticated, multi-source news aggregator that collects, analyzes, and summarizes news stories from diverse sources including RSS feeds, social media platforms, government sources, academic institutions, and industry publications. Built with Python and powered by advanced AI scoring algorithms.

## 🌟 Features

### **Multi-Source Collection**
- **RSS Feeds**: Major international news outlets (BBC, Guardian, CNN, NPR, etc.)
- **Social Media**: Reddit, Hacker News, Mastodon
- **Government Sources**: NASA, Government of Canada
- **Academic Institutions**: Harvard, MIT, UC Berkeley, Johns Hopkins, and more
- **Research Journals**: Nature, Science, The Lancet, PNAS, arXiv
- **Industry Publications**: TechCrunch, Wired, Ars Technica, Bloomberg

### **Advanced Content Analysis**
- **Quality Filtering**: Source reputation scoring and content quality assessment
- **Anti-Sensationalism**: Detects and penalizes clickbait and unreliable content
- **Smart Deduplication**: Fuzzy matching with source-aware verification
- **Geographic Diversity**: Ensures balanced global coverage
- **Impact Scoring**: Identifies truly important stories vs. viral content

### **Intelligent Story Selection**
- **Scarcity Detection**: Finds underreported important stories from reliable sources
- **Authenticity Scoring**: Rewards factual, evidence-based reporting
- **Source Hierarchy**: Prioritizes high-reputation sources
- **Diversity Balancing**: Prevents topic clustering and ensures variety

### **AI-Powered Summarization**
- **Cypher Alpha Integration**: Advanced LLM for intelligent report generation
- **Structured Output**: Organized by categories with source attribution
- **Comprehensive Coverage**: Politics, business, technology, science, health, and more

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tvanderb/news-aggregator.git
   cd news-aggregator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   ```bash
   cp config.example.json config.json
   # Edit config.json with your API keys
   ```

4. **Run the aggregator**
   ```bash
   python cronkite.py
   ```

## ⚙️ Configuration

Create a `config.json` file with your API credentials:

```json
{
  "cypher_api_key": "your_cypher_alpha_api_key",
  "newsapi_key": "your_newsapi_key",
  "hours_back": 24,
  "story_limit": 100
}
```

### Required API Keys
- **Cypher Alpha**: For AI-powered report generation
- **NewsAPI**: For additional news sources (optional)

## 📊 How It Works

### 1. **Data Collection Phase**
The aggregator concurrently fetches stories from all configured sources:
- RSS feeds are parsed for recent articles
- Social media platforms are scraped for trending content
- Government and academic sources provide authoritative updates
- NewsAPI supplements with categorized content

### 2. **Quality Assessment Phase**
Each story undergoes rigorous evaluation:
- **Source Reputation**: Domain-based reliability scoring
- **Content Quality**: Length, structure, and factual indicators
- **Anti-Sensationalism**: Detection of clickbait and unreliable language
- **Geographic Classification**: Ensures global diversity

### 3. **Advanced Scoring Phase**
Stories are scored using a multi-factor algorithm:
- **Source Quality** (40%): Reputation and reliability
- **Authenticity** (25%): Factual reporting indicators
- **Anti-Sensationalism** (-30%): Penalties for clickbait
- **Impact** (15%): Importance and significance
- **Scarcity** (10%): Uniqueness and underreporting
- **Recency** (10%): Timeliness

### 4. **Selection and Deduplication**
- Fuzzy matching identifies duplicate stories
- Source hierarchy determines preferred versions
- Diversity algorithms prevent topic clustering
- Top stories are selected based on comprehensive scoring

### 5. **AI Summarization**
Selected stories are sent to Cypher Alpha for:
- Intelligent categorization
- Concise summarization
- Source attribution
- Structured report generation

## 🏗️ Architecture

```
cronkite/
├── core.py              # Main aggregator logic
├── rss.py               # RSS feed processing
├── social.py            # Social media scraping
├── newsapi.py           # NewsAPI integration
├── specialized.py       # Government/academic sources
├── quality.py           # Quality filtering & scoring
├── report.py            # AI report generation
└── config.py            # Configuration & constants
```

### Key Components

- **NewsAggregator**: Orchestrates the entire collection and processing pipeline
- **StoryScorer**: Advanced scoring algorithms for story selection
- **QualityFilter**: Content quality and source reliability assessment
- **CypherReportGenerator**: AI-powered report creation

## 📈 Example Output

The aggregator generates comprehensive daily reports like:

```
# Legible News
July 3, 2025

## Politics and elections
• The US House of Representatives is voting on a procedural rule...
• A federal court has ruled that Donald Trump's asylum ban...

## Business and economy  
• The ADP report indicates that the US economy may have lost jobs...
• Alibaba has announced a $7 billion subsidy program...

## Armed conflicts and attacks
• Over 900 earthquakes have shaken Japan's Tokara islands...
• The Israeli military has been accused of using a 500lb bomb...
```

## 🔧 Customization

### Adding New Sources

1. **RSS Feeds**: Add to `RSS_FEEDS` in `config.py`
2. **Social Media**: Extend scrapers in `social.py`
3. **Government/Academic**: Add to specialized scrapers
4. **Domain Reputation**: Update `DOMAIN_REPUTATION` scores

### Adjusting Scoring Weights

Modify the scoring algorithm in `quality.py`:
```python
# Base source quality score (0-1) - heavily weighted
score += source_score * 0.4

# Authenticity score - new factor  
score += authenticity_score * 0.25

# Anti-sensationalism penalty - strict approach
score -= sensationalism_penalty * 0.3
```

### Filtering Content

- **Opinion Filtering**: Configure `OPINION_KEYWORDS` in `config.py`
- **Source Blocking**: Add domains to `UNRELIABLE_SOURCES`
- **Geographic Focus**: Adjust `GEOGRAPHIC_DIVERSITY` settings

## 🎯 Use Cases

- **News Monitoring**: Daily digest of important global events
- **Research**: Academic and scientific breakthrough tracking
- **Business Intelligence**: Market and industry trend analysis
- **Policy Analysis**: Government and regulatory updates
- **Content Creation**: Curated news for newsletters or blogs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 cronkite/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Cypher Alpha** for AI-powered report generation
- **NewsAPI** for additional news sources
- **Feedparser** for RSS processing
- **BeautifulSoup** for web scraping
- **PRAW** for Reddit integration
- **LegibleNews** for inspiration

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/news-aggregator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/news-aggregator/discussions)
