# Backend Stock Processing

import requests
from company_overview import get_company_overview
from balance_sheet import get_balance_sheet
from income_statement import get_income_statement
from cash_flow_statement import get_cash_flow_statement
from stock_price import get_stock_price
from pillar_evaluations import get_pillar_evaluations
# import json

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

# returns STRING of the current shares outstanding
def get_shares_outstanding(company_overview_dict):
    shares_outstanding = company_overview_dict["shares_outstanding"]
    return shares_outstanding

# returns STRING of the 5 year change in shares outstanding
def get_five_year_share_change(balance_sheet_dict):
    change_in_shares_outstanding = int(balance_sheet_dict["shares_outstanding"][0]) - int(balance_sheet_dict["shares_outstanding"][4])
    print()
    print(balance_sheet_dict["shares_outstanding"][0])
    print(balance_sheet_dict["shares_outstanding"][4])
    print("CHANGE" + str(change_in_shares_outstanding))
    print()
    return str(change_in_shares_outstanding)

# returns STRING of the current years free cash flow
def get_free_cash_flow_growth(cash_flow_dict):
    now_fcf = int(cash_flow_dict["operating_cash_flow"][0]) - int(cash_flow_dict["capital_expenditures"][0])
    then_fcf = int(cash_flow_dict["operating_cash_flow"][4]) - int(cash_flow_dict["capital_expenditures"][4])
    free_cash_flow_growth = now_fcf - then_fcf
    return str(free_cash_flow_growth)

# returns int for 5 avg fcf 
def get_avg_fcf(cash_flow_dict):
    avg_fcf = 0
    for i in range(5):
        # print(int(cash_flow_dict["operating_cash_flow"][i]) - int(cash_flow_dict["capital_expenditures"][i]))
        avg_fcf = avg_fcf + int(cash_flow_dict["operating_cash_flow"][i]) - int(cash_flow_dict["capital_expenditures"][i])
    # print(avg_fcf/5)
    return avg_fcf/5

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

def print_evaluations(evaluation_metrics):
    print("hello evaluations")
    for evaluation in evaluation_metrics:
        print(evaluation)


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
    print("Stock price: " + stock_price)

    pillars = get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict)
    print(pillars)
    exit()

    # set and print pe ratio
    pe_ratio = get_pe(company_overview_dict)
    print("PE: " + pe_ratio)
    # set and print profit margin
    profit_margin = get_profit_margin(company_overview_dict)
    print("Profit Margin: " + str(profit_margin))
    # set and print profit growth
    profit_growth = get_profit_growth(income_statement_dict)
    print("Profit Growth: " + profit_growth)
    # set and print revenue growth
    revenue_growth = get_revenue_growth(income_statement_dict)
    print("Revenue Growth: " + revenue_growth)
    # set and print current assets vs liabilites
    total_current_assets_vs_liabilities = get_current_assets_vs_liabilities(balance_sheet_dict)
    print("Total Current Assets vs Liabilities: " + total_current_assets_vs_liabilities)
    # set and print total assets vs liabilites
    total_assets_vs_liabilities = get_assets_vs_liabilities(balance_sheet_dict)
    print("Total Assets vs Liabilities: " + total_assets_vs_liabilities)
    # set and print shares outstanding
    shares_outstanding = get_shares_outstanding(company_overview_dict)
    print("Shares Outstanding: " + shares_outstanding)
    # set and print change in shares outstanding
    change_in_shares_outstanding = get_five_year_share_change(balance_sheet_dict)
    print("Change in Shares Outstanding: " + change_in_shares_outstanding)
    # set and print free cash flow growth
    free_cash_flow = get_free_cash_flow_growth(cash_flow_dict)
    print("Free Cash Flow Growth: " + free_cash_flow)
    # set and print change in free cash flow
    desired_pe = 5
    market_cap = company_overview_dict["market_capitalization"]
    fcf_cap_evaluation, fcf_price_evaluation = get_free_cash_flow_evaluation(cash_flow_dict, free_cash_flow, shares_outstanding, stock_price, market_cap, desired_pe)
    print("Change in Free Cash Flow: " + fcf_cap_evaluation, )
    evaluation_metrics = [stock_price, pe_ratio, profit_margin, profit_growth, revenue_growth, 
                            total_current_assets_vs_liabilities, total_assets_vs_liabilities, 
                            shares_outstanding, change_in_shares_outstanding, free_cash_flow,
                            fcf_cap_evaluation, fcf_price_evaluation]
    print_evaluations(evaluation_metrics) 


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

# notes 
# how to interface with multiple interfaces
    # brady and the front end


# functionalities 

    # comparing intrinsic value vs the actual value 

    # back testing TBD Method ------

    # stock predictor ------

    # NLP for stock analysts and back testing -------

    # need to check for 5 years of stock history --------

    # get graph information

    # print financials