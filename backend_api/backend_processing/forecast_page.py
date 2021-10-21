from .shares import get_share_change

def get_revenue_growth_avg(income_statement_dict):
    sum = 0
    for x in range(4):
        current_revenue = int(income_statement_dict["totalRevenue"][x])
        previous_revenue = int(income_statement_dict["totalRevenue"][x+1])
        revenue_growth = 100 * (current_revenue - previous_revenue) / previous_revenue
        sum += revenue_growth
    return_avg = sum / 5
    return str(return_avg)

def get_profit_growth_avg(income_statement_dict):
    sum = 0
    for x in range(4):
        current_profit = int(income_statement_dict["grossProfit"][0])
        previous_profit = int(income_statement_dict["grossProfit"][4])
        profit_growth = 100 * (current_profit - previous_profit) / previous_profit
        sum += profit_growth
    return_avg = sum / 5
    return str(return_avg)

def get_fcf_growth_avg(cash_flow_dict):
    sum = 0
    for x in range(4):
        current_fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
        previous_fcf = int(cash_flow_dict["operatingCashflow"][4]) - int(cash_flow_dict["capitalExpenditures"][4])
        fcf_growth = 100 * (current_fcf - previous_fcf) / previous_fcf
        sum += fcf_growth
    return_avg = sum / 5
    return str(return_avg)

def get_price_to_fcf(company_overview_dict, cash_flow_dict):
    market_cap = int(company_overview_dict["market_cap"])
    fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    price_fcf_ratio = market_cap / fcf
    return str(price_fcf_ratio)

def get_forecast_table(ticker, company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    forecast_dict = {}
    forecast_dict["revenue_growth"] = get_revenue_growth_avg(income_statement_dict)
    forecast_dict["change_in_shares_ourstanding"] = get_share_change(balance_sheet_dict, company_overview_dict)
    forecast_dict["profit_margin"] = get_profit_growth_avg(company_overview_dict)
    forecast_dict["fcf_growth"] = get_fcf_growth_avg(cash_flow_dict)
    forecast_dict["pe_ratio"] = company_overview_dict["pe_ratio"]
    forecast_dict["price_to_fcf"] = get_price_to_fcf(company_overview_dict, cash_flow_dict)
    forecast_dict["Annual Return"] = "---"

    return forecast_dict