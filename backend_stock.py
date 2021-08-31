# Backend Stock Processing

import requests
import json

def set_api_urls(api_urls, ticker, key):
    api_urls["daily_adjusted_url"] = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=' + key
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key

def get_company_overview(ticker):
    req = requests.get(api_urls["company_overview_url"])
    response = req.json()
    overview_dict = {
        'name' : response["Name"],
        'description' : response["Description"],
        'sector' : response["Sector"],
        'market_capitalization' : response["MarketCapitalization"],
        'pe_ratio' : response["PERatio"],
        'dividend_per_share' : response["DividendPerShare"],
        'dividend_yield' : response["DividendYield"],
        'profit_margin' : response["ProfitMargin"],
        'return_on_assets_ttm' : response["ReturnOnAssetsTTM"],
        'return_on_equity_ttm' : response["ReturnOnEquityTTM"],
        'analyst_target_price' : response["AnalystTargetPrice"],
        'week_52_high' : response["52WeekHigh"],
        'week_52_low' : response["52WeekLow"],
        'day_50_moving_avg' : response["50DayMovingAverage"],
        'day_200_moving_avg' : response["200DayMovingAverage"],
        'shares_outstanding' : response["SharesOutstanding"],
        'dividend_date' : response["DividendDate"],
        'exdividend_data' : response["ExDividendDate"]
    }
    # for key in overview_dict:
    #     print(key)
    #     print(overview_dict[key])
    return overview_dict

# get most recent stock price at close as a STRING
def get_stock_price(ticker):
    req = requests.get(api_urls["intraday_url"])
    response = req.json()
    # print(response)
    minute_data = response["Time Series (1min)"]
    latest_minute = next(iter(minute_data))
    latest_close_price = minute_data[latest_minute]["4. close"]
    # print("The stock price of " + ticker + " is " + latest_close_price)
    return latest_close_price

# returns pe ration as a STRING
def get_pe(company_overview_dict):
    pe_ratio = company_overview_dict["pe_ratio"]
    return pe_ratio

# returns profit margin as a percent as a FLOAT
def get_profit_margin(company_overview_dict):
    profit_margin = company_overview_dict["profit_margin"]
    # print(profit_margin)
    profit_margin = float(profit_margin) * 100
    return profit_margin


# def get_profit_growth():
# def get_revenue_growth():
# def get_current_assets_vs_liabilities():
# def get_shares_outstanding():
# def get_free_cash_flow_growth():
# def get_free_cash_flow_evaluation():


def evaluation_processing(ticker):
    # print("call evaluations on " + ticker)
    company_overview_dict = get_company_overview(ticker)
    stock_price = get_stock_price(ticker)
    print("Stock price: " + stock_price)
    pe_ratio = get_pe(company_overview_dict)
    print("PE: " + pe_ratio)
    profit_margin = get_profit_margin(company_overview_dict)
    print("Profit Margin: " + str(profit_margin))

def db_postions_processing():
    print("To be developed with Brady")

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
evaluation_processing(ticker)

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