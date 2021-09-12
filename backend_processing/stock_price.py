# returns STRING of most recent intraday close stock price to the most recent minute

import requests

def get_stock_price(ticker, api_urls):

    req = requests.get(api_urls["intraday_url"])
    response = req.json()
    minute_data = response["Time Series (1min)"]
    latest_minute = next(iter(minute_data))
    latest_close_price = minute_data[latest_minute]["4. close"]
    
    return latest_close_price