# Backend Stock Processing

import requests
import json

def set_api_urls(api_urls, ticker, key):
    api_urls["daily_adjusted_url"] = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=' + key

# get most recent stock price at close
def get_stock_price(ticker):
    req = requests.get(api_urls["daily_adjusted_url"])
    response = req.json()
    # print(response)
    day_data = response["Time Series (Daily)"]
    latest_day = next(iter(day_data))
    latest_close_price = day_data[latest_day]["4. close"]
    print(latest_close_price)

# def get_pe():
# def get_profit_margin():
# def get_profit_growth():
# def get_revenue_growth():
# def get_current_assets_vs_liabilities():
# def get_shares_outstanding():
# def get_free_cash_flow_growth():
# def get_free_cash_flow_evaluation():

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
key = open('./key.txt').read()
set_api_urls(api_urls, ticker, key)
# print(api_urls)

# call evaluations
call_evaluations(ticker)

# end
print("\nBackend Stock Processed ")


# notes 
# how to interface with multiple interfaces
    # brady and the front end

# CORNERSTONES
# pe ratio
# profit margin
# profit growth
# revenue growth
# current assets vs liabilities 
# shares outstanding
# cash flow growth
# cash flow * wanted pe ratio vs current market caps



# comparing intrinsic value vs the actual value 

# back testing TBD Method

# stock predictor

# NLP for stock analysts and back testing 