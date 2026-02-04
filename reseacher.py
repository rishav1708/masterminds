# researcher.py
from ddgs import DDGS

def get_latest_news(ticker):
    query = f"{ticker} stock news"
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
    headlines = [result["title"] for result in results]
    return headlines
