# Backend Stock Processing

import requests
import json

# returns DICTIONARY of urls, sets api urls based on passed ticker and key, 
def set_api_urls(api_urls, ticker, key):
    # api_urls["daily_adjusted_url"] = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=' + key
    api_urls["intraday_url"]=  'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + key
    api_urls["company_overview_url"] = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + key
    api_urls["balance_sheet_url"] = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + key
    api_urls["income_statement_url"] = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + key
    api_urls["cash_flow_url"] = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + key

###########################################

# returns a DICTIONARY of information to be used regarding company overview api request
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
    # print(overview_dict)
    return overview_dict

# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the balance sheet api request
def get_balance_sheet(ticker):
    req = requests.get(api_urls["balance_sheet_url"])
    response = req.json()
    annual_reports = response["annualReports"]
    # print(annual_reports)
    balance_sheet_dict = {}
    total_assests = []
    total_current_assets = []
    total_liabilities = []
    total_current_liabilities = []
    shares_outstanding = []
    for fiscal_report in annual_reports:
        total_assests.append(fiscal_report["totalAssets"])
        total_current_assets.append(fiscal_report["totalCurrentAssets"])
        total_liabilities.append(fiscal_report["totalLiabilities"])
        total_current_liabilities.append(fiscal_report["totalCurrentLiabilities"])
        shares_outstanding.append(fiscal_report["commonStockSharesOutstanding"])
    balance_sheet_dict["total_assets"] = total_assests
    balance_sheet_dict["total_current_assets"] = total_current_assets
    balance_sheet_dict["total_liabilities"] = total_liabilities
    balance_sheet_dict["total_current_liabilities"] = total_current_liabilities
    balance_sheet_dict["shares_outstanding"] = shares_outstanding
    # print(balance_sheet_dict)
    return balance_sheet_dict

# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the income statement api request
def get_income_statement(ticker):
    req = requests.get(api_urls["income_statement_url"])
    response = req.json()
    annual_reports = response["annualReports"]
    income_statement_dict = {}
    gross_profit = []
    total_revenue = []
    net_income = []
    for income_report in annual_reports:
        gross_profit.append(income_report["grossProfit"])
        total_revenue.append(income_report["totalRevenue"])
        net_income.append(income_report["netIncome"])
    income_statement_dict["gross_profit"] = gross_profit
    income_statement_dict["total_revenue"] = total_revenue
    income_statement_dict["net_income"] = net_income
    # print(income_statement_dict)
    return income_statement_dict

# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the cash flow statement api request
def get_cash_flow_statement(ticker):
    # Free Cash Flow = Operating Cash Flow − Capital Expenditures
    req = requests.get(api_urls["cash_flow_url"])
    response = req.json()
    annual_reports = response["annualReports"]
    cash_flow_dict = {}
    operating_cash_flow = []
    capital_expenditures = []
    for cash_flow_report in annual_reports:
        operating_cash_flow.append(cash_flow_report["operatingCashflow"])
        capital_expenditures.append(cash_flow_report["capitalExpenditures"])
    cash_flow_dict["operating_cash_flow"] = operating_cash_flow
    cash_flow_dict["capital_expenditures"] = capital_expenditures
    # print(cash_flow_dict)
    return cash_flow_dict

###########################################

# returns STRING of most recent intraday close stock price to the most recent minute
def get_stock_price(ticker):
    req = requests.get(api_urls["intraday_url"])
    response = req.json()
    minute_data = response["Time Series (1min)"]
    latest_minute = next(iter(minute_data))
    latest_close_price = minute_data[latest_minute]["4. close"]
    return latest_close_price

# returns STRING of the companies PE Ratio
def get_pe(company_overview_dict):
    pe_ratio = company_overview_dict["pe_ratio"]
    return pe_ratio

# returns STRING of the profit margin as a percentage
def get_profit_margin(company_overview_dict):
    profit_margin = company_overview_dict["profit_margin"]
    profit_margin = float(profit_margin) * 100.0
    return str(profit_margin)

# returns STRING of the profit growth over the last 5 years
def get_profit_growth(income_statement_dict):
    profit_growth = int(income_statement_dict["gross_profit"][0]) - int(income_statement_dict["gross_profit"][4])
    return str(profit_growth)

# returns STRING of the revenue growth over the last 5 years
def get_revenue_growth(income_statement_dict):
    revenue_growth = int(income_statement_dict["total_revenue"][0]) - int(income_statement_dict["total_revenue"][4])
    return str(revenue_growth)

# returns STRING of current assets vs liabilities
def get_current_assets_vs_liabilities(balance_sheet_dict):
    total_current_assets_vs_liabilities = int(balance_sheet_dict["total_current_assets"][0]) - int(balance_sheet_dict["total_current_liabilities"][0])
    return str(total_current_assets_vs_liabilities)

# returns STRING of total assets vs liabilities
def get_assets_vs_liabilities(balance_sheet_dict):
    total_assets_vs_liabilities = int(balance_sheet_dict["total_assets"][0]) - int(balance_sheet_dict["total_liabilities"][0])
    return str(total_assets_vs_liabilities)

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
def evaluation_processing(ticker):
    # make the necessary data dictionaries to make a stock recommendation
    company_overview_dict = get_company_overview(ticker)
    balance_sheet_dict = get_balance_sheet(ticker)
    income_statement_dict = get_income_statement(ticker)
    cash_flow_dict = get_cash_flow_statement(ticker)

    # set and print stock price
    stock_price = get_stock_price(ticker)
    print("Stock price: " + stock_price)
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

if __name__ == "__main__":
    # start
    print("\nBackend Stock Processing\n")

    # get ticker from user
    # this will need error checking, this will need to be passed from database or from front end ???
    ticker = input("Please enter a stock ticker: ")
    ticker = str(ticker)
    ticker = ticker.upper()
    # print(ticker)

    # set api urls 
    api_urls = {}
    key = open('./key.txt').read()
    set_api_urls(api_urls, ticker, key)
    # print(api_urls)

    # call evaluations, this would be from angular front end. implemented with flask api
    evaluation_processing(ticker)

    # call db process, this would be from the positions db, place holder
    print()
    db_postions_processing()

    # end
    print("\nBackend Stock Processed ")


# notes 
# how to interface with multiple interfaces
    # brady and the front end

# CORNERSTONES
    # pe ratio +
    # profit margin +
    # profit growth +
    # revenue growth +
    # current assets vs liabilities +
    # shares outstanding +
    # cash flow growth +
    # cash flow * wanted pe ratio vs current market caps +

# functionalities 
    # comparing intrinsic value vs the actual value 

    # back testing TBD Method ------

    # stock predictor ------

    # NLP for stock analysts and back testing -------

    # need to check for 5 years of stock history --------