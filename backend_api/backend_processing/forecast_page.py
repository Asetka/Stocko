from .shares import get_share_change_avg

def get_revenue_cagr(income_statement_dict):
    current_revenue = int(income_statement_dict["totalRevenue"][0])
    previous_revenue = int(income_statement_dict["totalRevenue"][4])
    math_step = current_revenue/previous_revenue
    revenue_cagr = pow(math_step, 1/4) - 1
    revenue_cagr = revenue_cagr * 100
    revenue_cagr = "{:.2f}".format(revenue_cagr)
    return str(revenue_cagr)

def get_profit_margin_cagr(income_statement_dict):
    sum = 0
    for x in range(5):
        income = int(income_statement_dict["netIncome"][x])
        revenue = int(income_statement_dict["totalRevenue"][x])
        sum = sum + (income/revenue)
    profit_margin = (sum / 5) * 100
    profit_margin = "{:.2f}".format(profit_margin)
    return str(profit_margin)

def get_fcf_growth_avg(cash_flow_dict, income_statement_dict):
    sum = 0
    for x in range(5):
        revenue = int(income_statement_dict["totalRevenue"][x])
        fcf = int(cash_flow_dict["operatingCashflow"][x]) - int(cash_flow_dict["capitalExpenditures"][x])
        sum = sum + (fcf/revenue)
    fcf_margin = (sum / 5) * 100
    fcf_margin = "{:.2f}".format(fcf_margin)
    return str(fcf_margin)

def get_price_to_fcf(company_overview_dict, cash_flow_dict):
    market_cap = int(company_overview_dict["market_cap"])
    fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    price_fcf_ratio = market_cap / fcf
    price_fcf_ratio = "{:.2f}".format(price_fcf_ratio)
    return str(price_fcf_ratio)

def get_forecast_table(ticker, company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    forecast_dict = {}
    
    years_of_history = len(balance_sheet_dict["reportedCurrency"])
    if years_of_history != 5:
        forecast_dict["years_of_history_error"] = True
        return forecast_dict
    else:
        forecast_dict["years_of_history_error"] = False

    forecast_dict["revenue_cagr"] = get_revenue_cagr(income_statement_dict)
    forecast_dict["share_change_avg"] = get_share_change_avg(balance_sheet_dict, company_overview_dict)
    forecast_dict["profit_margin_avg"] = get_profit_margin_cagr(income_statement_dict)
    forecast_dict["fcf_margin_avg"] = get_fcf_growth_avg(cash_flow_dict, income_statement_dict)
    forecast_dict["pe_ratio"] = company_overview_dict["pe_ratio"]
    forecast_dict["price_to_fcf"] = get_price_to_fcf(company_overview_dict, cash_flow_dict)
    forecast_dict["Annual Return"] = "---"

    return forecast_dict