# agents.py
from quant import get_stock_data
from researcher import get_latest_news
from analyst import analyze_sentiment

def run_analysis(ticker):
    stock_data = get_stock_data(ticker)
    headlines = get_latest_news(ticker)
    sentiment_results = analyze_sentiment(headlines)
    return {
        "ticker": ticker,
        "price": stock_data["price"],
        "change": stock_data["change"],
        "volume": stock_data["volume"],
        "news_sentiment": sentiment_results
    }
