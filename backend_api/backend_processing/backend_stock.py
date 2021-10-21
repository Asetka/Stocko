# Backend Stock Processing

import requests
import os
from .company_overview import get_company_overview
from .balance_sheet import get_balance_sheet
from .income_statement import get_income_statement
from .cash_flow_statement import get_cash_flow_statement
from .stock_price import get_stock_price
from .pillar_evaluations import get_pillar_evaluations
from .shares import get_shares_outstanding
from .forecast_page import get_forecast_table

# returns DICTIONARY of urls, sets api urls based on passed ticker and key, 
def set_api_urls_pillars(api_urls, ticker, key):
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key
    api_urls["balance_sheet_url"] = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + key
    api_urls["income_statement_url"] = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + key
    api_urls["cash_flow_url"] = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + key

# returns DICTIONARY of urls, sets api urls based on passed ticker and key, 
def set_api_urls_stockpage(api_urls, ticker, key):
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key
    api_urls["balance_sheet_url"] = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + key
    api_urls["income_statement_url"] = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + key
    api_urls["cash_flow_url"] = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + key
    # ONE MORE API CALL FOR THE CHART DATA

def set_api_urls_forecastpage(api_urls, ticker, key):
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["balance_sheet_url"] = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + key
    api_urls["income_statement_url"] = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + key
    api_urls["cash_flow_url"] = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key


###########################################
###########################################

# processing of a ticker request from the front end for pillar evaluations
def evaluation_processing(ticker, api_urls):
    # make the necessary data dictionaries to make a stock recommendation
    company_overview_dict = get_company_overview(ticker, api_urls)
    balance_sheet_dict = get_balance_sheet(ticker, api_urls)
    income_statement_dict = get_income_statement(ticker, api_urls)
    cash_flow_dict = get_cash_flow_statement(ticker, api_urls)

    # set and print stock price
    stock_price = get_stock_price(ticker, api_urls)
    print("Stock Price: " + stock_price, end = '\n\n')

    # set and print current shares outstanding 
    shares_outstanding = get_shares_outstanding(company_overview_dict)
    print("Shares Outstanding: " + shares_outstanding, end = '\n\n') 

    pillars = get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict)
    pillars["stock_price"] = stock_price
    pillars["market_cap"] = company_overview_dict["market_cap"]

    for pillar in pillars:
        print(pillar, '\t', pillars[pillar])
    return pillars

# processing of a ticker request from the front end for stock page
def create_stock_page(ticker, api_urls):
    # make the necessary data dictionaries to make a stock page
    company_overview_dict = get_company_overview(ticker, api_urls)
    balance_sheet_dict = get_balance_sheet(ticker, api_urls)
    income_statement_dict = get_income_statement(ticker, api_urls)
    cash_flow_dict = get_cash_flow_statement(ticker, api_urls)
    # ONE MORE API CALL FOR THE CHART DATA

    # get stock price
    stock_price = get_stock_price(ticker, api_urls)

    stock_page_dict = {}
    stock_page_dict["ticker"] = ticker
    stock_page_dict["stock_price"] = stock_price
    stock_page_dict["company_overview"] = company_overview_dict
    stock_page_dict["balance_sheet_dict"] = balance_sheet_dict
    stock_page_dict["income_statement_dict"] = income_statement_dict
    stock_page_dict["cash_flow_dict"] = cash_flow_dict
    # ONE MORE API CALL FOR THE CHART DATA

    return stock_page_dict

# processing of a ticker request from the front end for forecast page
def create_forecast_page(ticker, api_urls):
    # make the necessary data dictionaries to make a stock forecastor
    company_overview_dict = get_company_overview(ticker, api_urls)
    balance_sheet_dict = get_balance_sheet(ticker, api_urls)
    income_statement_dict = get_income_statement(ticker, api_urls)
    cash_flow_dict = get_cash_flow_statement(ticker, api_urls)

    # get stock price
    stock_price = get_stock_price(ticker, api_urls)

    forecast_page_dict = get_forecast_table(ticker, company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict)
    forecast_page_dict["stock_price"] = stock_price
    
    for item in forecast_page_dict:
        print(item, '\t', forecast_page_dict[item])
    return forecast_page_dict

###########################################
###########################################

def my_main(ticker, process):
    # start
    print("\nBackend Stock Processing\n")

    if (process == "PILLARS"):
        # set api urls 
        api_urls = {}
        key = open(os.getcwd() + '/backend_api/backend_processing/key.txt').read()
        set_api_urls_pillars(api_urls, ticker, key)
        # call evaluations, this would be from angular front end. implemented with flask api
        pillars = evaluation_processing(ticker, api_urls)
        # end
        print("\nBackend Stock Processed\n")

        return pillars

    if (process == "STOCK PAGE"):
        # set api urls
        api_urls = {}
        key = open(os.getcwd() + '/backend_api/backend_processing/key.txt').read()
        set_api_urls_stockpage(api_urls, ticker, key)
        # create data dictionary for the stock page
        stock_page = create_stock_page(ticker, api_urls)
        # end
        print("\nBackend Stock Processed\n")
        return stock_page

    if (process == "FORECAST PAGE"):
        # set api urls
        api_urls = {}
        key = open(os.getcwd() + '/backend_api/backend_processing/key.txt').read()
        set_api_urls_forecastpage(api_urls, ticker, key)
        # create data dictionary for the stock page
        forecast_page = create_forecast_page(ticker, api_urls)
        # end
        print("\nBackend Stock Processed\n")
        return forecast_page

    return



