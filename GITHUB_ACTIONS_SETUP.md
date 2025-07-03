# GitHub Actions Setup Guide

This guide will help you set up automated daily news aggregation using GitHub Actions.

## 🚀 Quick Start

### 1. Choose Your Workflow

You have two workflow options:

- **Basic**: `.github/workflows/daily-news.yml` - Simple artifact generation
- **Advanced**: `.github/workflows/daily-news-advanced.yml` - Includes GitHub issues and email notifications

### 2. Set Up GitHub Secrets

Go to your repository → Settings → Secrets and variables → Actions, then add these secrets:

#### Required Secrets
```
CYPHER_API_KEY=your_cypher_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

#### Optional Secrets (for Advanced workflow)
```
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_TO=recipient@example.com
```

### 3. Enable the Workflow

The workflow will automatically run every day at 6:05 AM EST (11:05 AM UTC). You can also trigger it manually from the Actions tab.

## 📋 Detailed Setup Instructions

### Step 1: Get Your API Keys

#### Cypher API Key
1. Go to [OpenRouter](https://openrouter.ai/)
2. Sign up/login and get your API key
3. Copy the key to use in GitHub secrets

#### NewsAPI Key
1. Go to [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key from the dashboard

### Step 2: Configure GitHub Secrets

1. Navigate to your GitHub repository
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `CYPHER_API_KEY` | `your_cypher_key` | Your OpenRouter Cypher API key |
| `NEWSAPI_KEY` | `your_newsapi_key` | Your NewsAPI key |

### Step 3: Email Setup (Advanced Workflow Only)

If you want email notifications, you'll need to set up an app password:

#### Gmail Setup
1. Enable 2-factor authentication on your Google account
2. Go to [Google Account Settings](https://myaccount.google.com/apppasswords)
3. Generate an app password for "Mail"
4. Use this password (not your regular Gmail password) in the `EMAIL_PASSWORD` secret

#### Additional Email Secrets
| Secret Name | Value | Description |
|-------------|-------|-------------|
| `EMAIL_USERNAME` | `your_email@gmail.com` | Your Gmail address |
| `EMAIL_PASSWORD` | `your_app_password` | Gmail app password |
| `EMAIL_TO` | `recipient@example.com` | Where to send notifications |

### Step 4: Test the Workflow

1. Go to the **Actions** tab in your repository
2. Select the workflow you want to test
3. Click **Run workflow** → **Run workflow**
4. Monitor the execution and check the artifacts

## 📅 Schedule Configuration

The workflow runs at **6:05 AM EST** daily. To change the schedule:

### Time Zone Conversion
- **EST (UTC-5)**: 6:05 AM = 11:05 AM UTC
- **PST (UTC-8)**: 6:05 AM = 2:05 PM UTC
- **CET (UTC+1)**: 6:05 AM = 5:05 AM UTC

### Modify the Cron Expression
In the workflow file, change this line:
```yaml
- cron: '5 11 * * *'  # 11:05 AM UTC (6:05 AM EST)
```

Cron format: `minute hour day month day-of-week`

Examples:
- `'0 6 * * *'` - 6:00 AM UTC daily
- `'30 14 * * *'` - 2:30 PM UTC daily
- `'0 9 * * 1-5'` - 9:00 AM UTC weekdays only

## 📦 Artifacts and Outputs

### What Gets Generated
1. **News Report** (`news_report.txt`) - The actual news summary (stored as artifact)
2. **Logs** (`logs/cronkite.log`) - Detailed execution logs (not stored as artifact)
3. **GitHub Issue** (Advanced workflow) - Daily report as an issue
4. **Email Notification** (Advanced workflow) - Status email

### Accessing Artifacts
1. Go to **Actions** tab
2. Click on a workflow run
3. Scroll down to **Artifacts**
4. Download the `daily-news-report-{number}` artifact containing the news report

**Note**: Logs are generated but not stored as artifacts to keep artifact size minimal. If you need logs for debugging, you can modify the workflow to include them.

### Artifact Retention
- Artifacts are kept for **30 days**
- You can modify this in the workflow file:
```yaml
retention-days: 30  # Change this number
```

## 🔧 Customization Options

### Modify Configuration
Edit the config generation in the workflow:

```yaml
- name: Create config file
  run: |
    cat > config.json << EOF
    {
      "cypher_api_key": "${{ secrets.CYPHER_API_KEY }}",
      "newsapi_key": "${{ secrets.NEWSAPI_KEY }}",
      "hours_back": 24,        # Change this
      "story_limit": 150,      # Change this
      "log_level": "INFO",     # Change this
      "log_file": "logs/cronkite.log",
      "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
      "disable_console": false # Change this
    }
    EOF
```

### Add More Output Formats
You can modify the workflow to generate different output formats:

```yaml
- name: Generate JSON output
  run: |
    python -c "
    import json
    from cronkite.core import NewsAggregator
    import asyncio
    
    async def main():
        aggregator = NewsAggregator()
        stories = await aggregator.collect_all_stories(hours_back=24, limit=100)
        data = [story.to_dict() for story in stories]
        with open('news_data.json', 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    asyncio.run(main())
    "
```

## 🚨 Troubleshooting

### Common Issues

#### 1. API Key Errors
- **Error**: "Invalid API key"
- **Solution**: Check that your secrets are correctly set in GitHub

#### 2. Dependencies Missing
- **Error**: "Module not found"
- **Solution**: Ensure `requirements.txt` is up to date

#### 3. Permission Issues
- **Error**: "Permission denied"
- **Solution**: Check that the workflow has access to create issues (for advanced workflow)

#### 4. Email Not Sending
- **Error**: "SMTP authentication failed"
- **Solution**: Use app password, not regular Gmail password

### Debug Steps
1. Check the workflow logs in the Actions tab
2. Verify all secrets are set correctly
3. Test the script locally first
4. Check the generated artifacts for error details

## 📊 Monitoring and Maintenance

### Check Workflow Status
- Go to **Actions** tab to see recent runs
- Green checkmark = success
- Red X = failure

### Review Logs
- Download the log artifacts to debug issues
- Look for error messages in the workflow summary

### Update Dependencies
- Keep `requirements.txt` updated
- Test locally before pushing changes

## 🔒 Security Considerations

### API Key Security
- Never commit API keys to the repository
- Use GitHub secrets for all sensitive data
- Rotate keys periodically

### Email Security
- Use app passwords, not regular passwords
- Consider using a dedicated email for notifications
- Monitor for unusual activity

### Repository Security
- Limit workflow permissions if possible
- Review workflow changes before merging
- Monitor for unauthorized workflow runs

## 📈 Advanced Features

### Multiple Schedules
You can run the workflow multiple times per day:

```yaml
on:
  schedule:
    - cron: '5 11 * * *'   # 6:05 AM EST
    - cron: '5 18 * * *'   # 1:05 PM EST
```

### Conditional Execution
Run only on weekdays:

```yaml
- cron: '5 11 * * 1-5'  # Monday-Friday only
```

### Different Configurations
Create multiple workflows for different purposes:
- Morning news summary
- Evening news summary
- Weekend special reports

## 🎯 Next Steps

1. **Set up the basic workflow first**
2. **Test with manual triggers**
3. **Add email notifications if desired**
4. **Customize the schedule and configuration**
5. **Monitor and optimize based on results**

The workflow will automatically start running daily once you've set up the secrets and pushed the workflow files to your repository! 