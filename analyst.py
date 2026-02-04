# analyst.py
from transformers import pipeline

sentiment_model = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

def analyze_sentiment(headlines):
    results = []
    for headline in headlines:
        sentiment = sentiment_model(headline)
        results.append({
            "headline": headline,
            "sentiment": sentiment[0]["label"],
            "score": sentiment[0]["score"]
        })
    return results
