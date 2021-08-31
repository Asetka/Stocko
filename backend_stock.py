# Backend Stock Processing

import requests
import json


# comparing intrinsic value vs the actual value 

# CORNERSTONES
# pe ratio
# profit margin
# profit growth
# revenue growth
# current assets vs liabilities 
# shares outstanding
# cash flow growth
# cash flow * wanted pe ratio vs current market cap


# back testing TBD Method

# stock predictor

# NLP for stock analysts and back testing 

def set_api_urls(api_urls, ticker):
    api_urls["daily_adjusted_url"] = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=demo'

# get most recent stock price at close
def get_stock_price(ticker):
    req = requests.get(api_urls["daily_adjusted_url"])
    response = req.json()
    day_data = response["Time Series (Daily)"]
    latest_day = next(iter(day_data))
    latest_close_price = day_data[latest_day]["4. close"]
    print(latest_close_price)


def call_evaluations(ticker):
    print("call evaluations on " + ticker)
    get_stock_price(ticker)

# start
print("Backend Stock Processing\n")

# get ticker from user, no error checking yet
ticker = input("Please enter a stock ticker: ")
ticker = str(ticker)
ticker = ticker.upper()
print(ticker)

# set api urls 
api_urls = {}
set_api_urls(api_urls, ticker)
# print(api_urls)

# call evaluations
call_evaluations(ticker)

# end
print("\nBackend Stock Processed ")