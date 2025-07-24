# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            source TEXT,
            url TEXT UNIQUE,
            published_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_articles(df):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO news_articles (title, author, source, url, published_at)
                VALUES (?, ?, ?, ?, ?)
            """, (row.title, row.author, row.source, row.url, row.published_at))
        except sqlite3.IntegrityError:
            continue  # Skip duplicates
    conn.commit()
    conn.close()
