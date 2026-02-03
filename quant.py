import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    if hist.empty:
        return None
    data = {
        "ticker": ticker,
        "price": hist["Close"].iloc[-1],
        "change": hist["Close"].iloc[-1] - hist["Open"].iloc[-1],
        "volume": hist["Volume"].iloc[-1],
    }
    return data

if __name__ == "__main__":
    print(get_stock_data("AAPL"))
