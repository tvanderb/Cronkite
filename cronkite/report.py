import aiohttp
import json
from typing import Dict

class CypherReportGenerator:
    """Generate final report using OpenRouter Cypher Alpha"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
    
    async def generate_report(self, news_data: Dict) -> str:
        """Generate Legible News style report using Cypher Alpha"""
        
        prompt = f"""You are a news summarizer. Please create a daily news report in the exact style of Legible News, using the following news stories collected from various sources:

{json.dumps(news_data, indent=2, default=str)}

Format requirements:
1. Group stories by category (Armed conflicts and attacks, Disasters and accidents, Politics and elections, Law and crime, etc.).
2. Each story should be a single bullet point with the main headline, key details, and source citation(s) in parentheses.
3. If multiple sources report the same event, merge them into a single bullet and cite all sources in parentheses.
4. Do not repeat the same story in multiple categories. If a story fits multiple categories, choose the most relevant one.
5. Use clean, factual, neutral, and journalistic language similar to Wikipedia.
6. Include relevant hyperlinks (use the provided URLs).
7. Focus on the most significant and recent stories. If there are many stories in one category, select only the most significant.
8. Aim to include a mix of sources and regions when possible.
9. Limit to about 45-65 total stories.
10. Start with today's date.

Example format:

Armed conflicts and attacks
• [Summary of event] ([Source1], [Source2])
• [Summary of event] ([Source])

Politics and elections
• [Summary of event] ([Source])

[Insert the actual data here]

Make this look exactly like the Legible News format you've seen before."""
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
            'HTTP-Referer': 'https://your-app-name.com',  # Replace with your app name
            'X-Title': 'News Aggregator'  # Optional: your app title
        }
        
        payload = {
            'model': 'openrouter/cypher-alpha:free',
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': 4000,
            'temperature': 0.7,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=headers, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['message']['content']
                else:
                    error_text = await response.text()
                    raise Exception(f"OpenRouter API error: {response.status} - {error_text}") 