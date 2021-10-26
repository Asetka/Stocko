from .shares import get_share_change

def get_revenue_cagr(income_statement_dict):
    current_revenue = int(income_statement_dict["totalRevenue"][0])
    previous_revenue = int(income_statement_dict["totalRevenue"][4])
    math_step = current_revenue/previous_revenue
    revenue_cagr = pow(math_step, 1/4) - 1
    revenue_cagr = revenue_cagr * 100
    return str(revenue_cagr)

def get_profit_cagr(income_statement_dict):
    current_profit = int(income_statement_dict["grossProfit"][0])
    previous_profit = int(income_statement_dict["grossProfit"][4])
    math_step = current_profit/previous_profit
    profit_cagr = pow(math_step, 1/4) - 1
    profit_cagr = profit_cagr * 100
    return str(profit_cagr)

def get_fcf_growth_avg(cash_flow_dict):
    sum = 0
    for x in range(4):
        current_fcf = int(cash_flow_dict["operatingCashflow"][x]) - int(cash_flow_dict["capitalExpenditures"][x])
        previous_fcf = int(cash_flow_dict["operatingCashflow"][x+1]) - int(cash_flow_dict["capitalExpenditures"][x+1])
        fcf_growth = 100 * (current_fcf - previous_fcf) / previous_fcf
        sum += fcf_growth
    return_avg = sum / 4
    return str(return_avg)

def get_price_to_fcf(company_overview_dict, cash_flow_dict):
    market_cap = int(company_overview_dict["market_cap"])
    fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    price_fcf_ratio = market_cap / fcf
    return str(price_fcf_ratio)

def get_forecast_table(ticker, company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    forecast_dict = {}
    forecast_dict["revenue_cagr"] = get_revenue_cagr(income_statement_dict)
    # forecast_dict["change_in_shares_ourstanding_avg"] = get_share_change(balance_sheet_dict, company_overview_dict)
    forecast_dict["profit_cagr"] = get_profit_cagr(income_statement_dict)
    forecast_dict["fcf_growth_avg"] = get_fcf_growth_avg(cash_flow_dict)
    forecast_dict["pe_ratio"] = company_overview_dict["pe_ratio"]
    forecast_dict["price_to_fcf"] = get_price_to_fcf(company_overview_dict, cash_flow_dict)
    forecast_dict["annual_return"] = "---"

    return forecast_dict