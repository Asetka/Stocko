# returns STRING of most recent intraday close stock price to the most recent minute

import requests

def get_stock_price(ticker, api_urls):

    req = requests.get(api_urls["intraday_url"])
    response = req.json()
    minute_data = response["Time Series (5min)"]
    latest_minute = next(iter(minute_data))
    latest_close_price = minute_data[latest_minute]["4. close"]
    latest_close_price = float(latest_close_price)
    latest_close_price = "{:.2f}".format(latest_close_price)
    return str(latest_close_price)