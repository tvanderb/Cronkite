# Cronkite News Aggregator

Automated news aggregation system that collects, filters, and generates daily reports from multiple sources.

[![Daily News Aggregation](https://github.com/tvanderb/Cronkite/workflows/Daily%20News%20Aggregation/badge.svg)](https://github.com/tvanderb/Cronkite/actions)

## 📰 Latest Report

**Latest Daily Report:** [View Latest Run](https://github.com/tvanderb/Cronkite/actions)

**Last Updated:** 2025-07-03 05:20 UTC

*Generated daily at 6:05 AM EST*

### 📋 Report Preview
```
July 3, 2025

Armed conflicts and attacks
• A New York jury found Sean "Diddy" Combs guilty on two counts related to bribery and falsifying business records, but not guilty on three more serious sex-trafficking charges. His lawyers called the verdict a "great victory." ([Guardian](https://www.theguardian.com/music/2025/jul/02/diddy-trial-verdict-sean-combs))
• The Pentagon halted shipments of Patriot air defense systems and other precision weapons to Ukraine due to concerns about low US stockpiles, prompting alarm in Kyiv. ([Guardian](https://www.theguardian.com/world/2025/jul/02/us-halts-ukraine-weapons-shipments))
• Donald Trump's proclamation of an "invasion" at the US-Mexico border was ruled unlawful by a federal court, which said he exceeded his authority in suspending asylum rights. ([Guardian](https://www.theguardian.com/us-news/2025/jul/02/trump-us-mexico-border-immigrants-asylum))

Politics and elections
• Donald Trump’s signature tax-and-spending bill hangs in the balance in the US House of Representatives as Republicans struggle to muster sufficient votes. ([Guardian](https://www.theguardian.com/us-news/2025/jul/02/trump-bill-house-senate))
• The acting chair of Creative Australia apologized to artist Khaled Sabsabi for the "hurt and pain" caused after his work was initially withdrawn from the Venice Biennale. ([Guardian](https://www.theguardian.com/artanddesign/2025/jul/03/creative-australia-apologises-to-khaled-sabsabi-for-hurt-and-pain-after-venice-biennale-reinstatement-ntwnfb))
• Labour's 10-year health plan to shift NHS care from hospitals to new community health centers in England was met with mixed reactions. ([Guardian](https://www.theguardian.com/politics/2025/jul/02/will-labours-10-year-health-plan-usher-in-a-new-era-for-the-nhs-in-england))

International relations
• China rolled out a record-setting 500-megawatt turbine for a hydropower plant in Tibet, marking the world's largest single-unit capacity. ([SCMP](https://www.scmp.com/news/china/science/article/3316685/china-rolls-out-record-setting-turbine-tibet-hydropower-plant?utm_source=rss_feed))
• Lorde fans expressed frustration as her new translucent CD reportedly didn't play on some CD players. ([Vice](https://www.vice.com/en/article/lorde-fans-are-complaining-that-her-new-translucent-cd-wont-play-on-their-cd-players/))
• A man in China honored his farmer father at his graduation ceremony by dressing him in an academic gown. ([SCMP](https://www.scmp.com/news/people-culture/trending-china/article/3315900/china-graduate-honours-dad-ceremony-dressing-him-academic-gown-touches-hearts?utm_source=rss_feed))

Law and crime
• Met Police in London were accused of abusing their powers to curb protests after research found that less than 3% of arrests for conspiracy to cause a public nuisance in the past five years resulted in prosecution. ([Guardian](https://www.theguardian.com/uk-news/2025/jul/03/met-police-accused-of-assault-on-right-to-protest-after-tenfold-rise-in-nuisance-law-arrests))
• Kilmar Ábrego García, a Maryland man wrongfully deported to El Salvador, was physically and psychologically tortured in a Salvadorian prison, according to new court documents. ([Guardian](https://www.theguardian.com/us-news/2025/jul/02/kilmar-abrego-garcia-tortured-cecot))

Business and economy
• Hong Kong developer Emperor International Holdings' struggles reflect the current state of Hong Kong's property sector, which has seen prices and rents fluctuate in recent years. ([SCMP](https://www.scmp.com/business/article/3316696/emperors-financial-struggle-mirrors-current-state-hong-kongs-property-sector?utm_source=rss_feed))
• Alibaba Group announced a $7 billion subsidy program for its instant commerce service, intensifying competition in China's on-demand delivery sector. ([SCMP](https://www.scmp.com/tech/big-tech/article/3316646/alibabas-us7-billion-subsidy-deepens-chinas-instant-e-commerce-war-jdcom-meituan?utm_source=rss_feed))

Disasters and accidents
• More than 900 earthquakes have shaken Japan's Tokara Islands in the past two weeks, leaving residents fearful of potential major damage. ([Guardian](https://www.theguardian.com/world/2025/jul/03/japan-earthquake-tokara-islands-900-earthquakes-two-weeks))
• Hong Kong tourists remain undeterred by a manga artist's prediction of a mega-earthquake in Japan on July 5, with no widespread cancellations of tour groups. ([SCMP](https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3316710/hong-kong-tourists-undeterred-manga-prediction-quake-will-hit-japan-july-5?utm_source=rss_feed))
Exit code: 0
Report generated at: Thu Jul  3 05:20:20 UTC 2025
```

### 📥 Download
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-2025-07-03` artifact
1. Click the badge above → Actions tab
2. Select latest "Daily News Aggregation" run
3. Download `daily-news-report-<YYYY-MM-DD>` artifact

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
