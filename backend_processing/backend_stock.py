# Backend Stock Processing

import requests
from company_overview import get_company_overview
from balance_sheet import get_balance_sheet
from income_statement import get_income_statement
from cash_flow_statement import get_cash_flow_statement
from stock_price import get_stock_price
from pillar_evaluations import get_pillar_evaluations
from shares import get_shares_outstanding

# returns DICTIONARY of urls, sets api urls based on passed ticker and key, 
def set_api_urls(api_urls, ticker, key):
    # api_urls["daily_adjusted_url"] = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=' + key
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key
    api_urls["balance_sheet_url"] = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + key
    api_urls["income_statement_url"] = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + key
    api_urls["cash_flow_url"] = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + key

###########################################
###########################################

# returns STRING of the 5 year change in shares outstanding
def get_five_year_share_change(balance_sheet_dict):
    change_in_shares_outstanding = int(balance_sheet_dict["shares_outstanding"][0]) - int(balance_sheet_dict["shares_outstanding"][4])
    print()
    print(balance_sheet_dict["shares_outstanding"][0])
    print(balance_sheet_dict["shares_outstanding"][4])
    print("CHANGE" + str(change_in_shares_outstanding))
    print()
    return str(change_in_shares_outstanding)


# returns STRING of the 5 year change in free cash flow
def get_free_cash_flow_evaluation(cash_flow_dict, free_cash_flow, shares_outstanding, stock_price, market_cap, desired_pe):
    print("\n\n")
    # need to get the 5 yr avg fcf
    avg_fcf = get_avg_fcf(cash_flow_dict)
    print()
    # print(avg_fcf)
    desired_market_cap = avg_fcf * int(desired_pe)
    print("Desired Market Cap = ", desired_market_cap)
    desired_share_price = desired_market_cap / int(shares_outstanding)
    print("Desired Share Price = ", desired_share_price)
    print()
    print("Current Market Cap = ", market_cap)
    # print(int(market_cap)/int(shares_outstanding))
    print("Current Stock Price = ", stock_price)
    print()
    # print("Check FCF/SHARES = ", int(free_cash_flow)/int(shares_outstanding))
    # print("Stock Price = " + stock_price)
    # exit()
    return str(desired_market_cap), str(desired_share_price)


# processing of a ticker request from the front end
def evaluation_processing(ticker, api_urls):
    # make the necessary data dictionaries to make a stock recommendation
    company_overview_dict = get_company_overview(ticker, api_urls)
    # print(company_overview_dict)
    balance_sheet_dict = get_balance_sheet(ticker, api_urls)
    # print(balance_sheet_dict)
    income_statement_dict = get_income_statement(ticker, api_urls)
    # print(income_statement_dict)
    cash_flow_dict = get_cash_flow_statement(ticker, api_urls)
    # print(cash_flow_dict)

    # set and print stock price
    stock_price = get_stock_price(ticker, api_urls)
    print("Stock Price: " + stock_price, end = '\n\n')

    # set and print current shares outstanding 
    shares_outstanding = get_shares_outstanding(company_overview_dict)
    print("Shares Outstanding: " + shares_outstanding, end = '\n\n') 

    pillars = get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict)
    print(pillars, end = '\n\n')
    exit()

    # set and print change in shares outstanding
    change_in_shares_outstanding = get_five_year_share_change(balance_sheet_dict)
    print("Change in Shares Outstanding: " + change_in_shares_outstanding)

# used to interface with the postions db
def db_postions_processing():
    print("To be developed with Brady")
    # print(get_stock_price(ticker))
    # exit()

if __name__ == "__main__":
    # start
    print("\nBackend Stock Processing\n")

    # get ticker from user
    # this will need error checking, this will need to be passed from database or from front end ???
    ticker = input("Please enter a stock ticker: ")
    ticker = str(ticker)
    ticker = ticker.upper()

    # set api urls 
    api_urls = {}
    key = open('./key.txt').read()
    set_api_urls(api_urls, ticker, key)
    # print(api_urls)

    # call evaluations, this would be from angular front end. implemented with flask api
    evaluation_processing(ticker, api_urls)

    # call db process, this would be from the positions db, place holder
    print()
    db_postions_processing()

    # end
    print("\nBackend Stock Processed ")

    exit(1)


