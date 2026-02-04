# app.py
import streamlit as st
import requests
import plotly.express as px
import yfinance as yf
from agents import run_analysis

st.set_page_config(page_title="MarketMinds", page_icon="📈", layout="wide")
st.title("MarketMinds: Real-Time Financial Analyst")

ticker = st.text_input("Enter stock ticker (e.g., RELIANCE.NS):")

if st.button("Analyze"):
    with st.spinner("Fetching data and analyzing..."):
        summary = run_analysis(ticker)

    st.subheader(f"Analysis for {ticker}")
    st.write(f"**Price:** ₹{summary['price']:.2f}")
    st.write(f"**Change:** ₹{summary['change']:.2f}")
    st.write(f"**Volume:** {summary['volume']:,}")

    st.subheader("Latest News Sentiment")
    for item in summary["news_sentiment"]:
        st.write(f"- {item['headline']} ({item['sentiment']}, {item['score']:.2f})")
