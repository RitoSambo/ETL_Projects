
import requests
import pandas as pd
from datetime import datetime

API_KEY = "fdf4161fdc9c45a29b7d4ea4549d55ea"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

def fetch_news():
    response = requests.get(NEWS_URL)
    articles = response.json().get("articles", [])

    data = []
    for article in articles:
        data.append({
            "title": article["title"],
            "author": article.get("author"),
            "source": article["source"]["name"],
            "url": article["url"],
            "published_at": article["publishedAt"]
        })

    df = pd.DataFrame(data)
    df.dropna(subset=["title", "url"], inplace=True)
    return df
