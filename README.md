# Cronkite

A Python-based news aggregator that collects, deduplicates, and summarizes news stories from RSS feeds, social media, and more. Generates a daily report using an LLM (Cypher Alpha).

## Setup

1. **Clone the repository**

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Copy and edit the config file:**
   ```bash
   cp config.json config.json.backup
   # Edit config.json and add your Cypher API key
   ```

5. **Run the aggregator:**
   ```bash
   python news_aggregator.py
   ```

## Configuration
- Edit `config.json` to set your API key and adjust parameters like `hours_back` and `story_limit`.
- Do not share your API key publicly.

## Notes
- The aggregator collects from a variety of sources, including RSS, Reddit, Hacker News, and Mastodon.
- Results are deduplicated and ranked by source reliability and recency.
- The report is generated using the Cypher Alpha LLM via OpenRouter.

---

Feel free to contribute or suggest new sources! 