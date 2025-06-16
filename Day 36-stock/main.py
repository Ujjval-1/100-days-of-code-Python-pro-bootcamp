import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_STOCK = os.getenv("API_KEY_STOCK")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")

STOCK_NAME = "MSFT"  # Tesla on NASDAQ, prices in USD
COMPANY_NAME = "Microsoft Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_daily_stock_data(symbol):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY_STOCK,
        "outputsize": "compact",
        "datatype": "json"
    }
    response = requests.get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()

    time_series = data.get("Time Series (Daily)")
    if not time_series:
        raise Exception("Stock data not found.")

    sorted_dates = sorted(time_series.keys(), reverse=True)
    latest = sorted_dates[0]
    previous = sorted_dates[1]

    latest_close = float(time_series[latest]["4. close"])
    previous_close = float(time_series[previous]["4. close"])

    return latest_close, previous_close, latest, previous

def get_top_news(company_name):
    news_params = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": company_name,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    return response.json().get("articles", [])[:3]

latest_close, previous_close, latest_date, prev_date = get_daily_stock_data(STOCK_NAME)

difference = latest_close - previous_close
arrow = "🔺" if difference > 0 else "🔻"
percent_change = abs(difference) / previous_close * 100

print(f"\n{STOCK_NAME} Price Movement")
print(f"{prev_date}: ${previous_close:.2f}")
print(f"{latest_date}: ${latest_close:.2f}")
print(f"Change: {arrow}{percent_change:.2f}%")

if percent_change > 5:
    print("\nSignificant change detected! Fetching news...")
    articles = get_top_news(COMPANY_NAME)

    for article in articles:
        print("\n--- News Article ---")
        print(f"Headline: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
else:
    print("\nNo significant change (>5%). Skipping news.")
