# scheduler.py
import schedule
import time
from fetch_news import fetch_news
from db import insert_articles, init_db

def job():
    print("Fetching news...")
    df = fetch_news()
    insert_articles(df)
    print("Inserted new articles.")

if __name__ == "__main__":
    init_db()
    schedule.every(10).minutes.do(job)
    job()  # Run once on startup
    while True:
        schedule.run_pending()
        time.sleep(1)
