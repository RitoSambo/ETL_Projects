# app.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, source, url, published_at FROM news_articles ORDER BY published_at DESC LIMIT 20")
    articles = cursor.fetchall()
    conn.close()
    return render_template("index.html", articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
