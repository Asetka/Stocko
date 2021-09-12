# pillar evaluations

from fcf_evaluation import get_fcf_evaluation

# returns STRING of the companies PE Ratio
def get_pe(company_overview_dict):
    pe_ratio = company_overview_dict["pe_ratio"]
    return pe_ratio

# returns STRING of the profit margin
def get_profit_margin(company_overview_dict):
    profit_margin = company_overview_dict["profit_margin"]
    profit_margin = float(profit_margin) * 100.0
    return str(profit_margin)

# returns STRING of the profit growth as a PERCENTAGE over the last 5 years
def get_profit_growth(income_statement_dict):
    current_profit = int(income_statement_dict["grossProfit"][0])
    previous_profit = int(income_statement_dict["grossProfit"][4])
    profit_growth = 100 * (current_profit - previous_profit) / previous_profit
    return str(profit_growth)

# returns STRING of the revenue growth as a PERCENTAGE over the last 5 years
def get_revenue_growth(income_statement_dict):
    current_revenue = int(income_statement_dict["totalRevenue"][0])
    previous_revenue = int(income_statement_dict["totalRevenue"][4])
    revenue_growth = 100 * (current_revenue - previous_revenue) / previous_revenue
    return str(revenue_growth)

# returns STRING of current assets vs liabilities
def get_current_assets_vs_liabilities(balance_sheet_dict):
    total_current_assets_vs_liabilities = int(balance_sheet_dict["totalCurrentAssets"][0]) - int(balance_sheet_dict["totalCurrentLiabilities"][0])
    return str(total_current_assets_vs_liabilities)

# returns STRING of total assets vs liabilities
def get_total_assets_vs_liabilities(balance_sheet_dict):
    total_assets_vs_liabilities = int(balance_sheet_dict["totalAssets"][0]) - int(balance_sheet_dict["totalLiabilities"][0])
    return str(total_assets_vs_liabilities)

# returns STRING of the fcf growth as a PERCENTAGE over the last 5 years
def get_fcf_growth(cash_flow_dict):
    current_fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    previous_fcf = int(cash_flow_dict["operatingCashflow"][4]) - int(cash_flow_dict["capitalExpenditures"][4])
    fcf_growth = 100 * (current_fcf - previous_fcf) / previous_fcf
    return str(fcf_growth)


def get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    pillars = {}
    pillars["pe_ratio"] = get_pe(company_overview_dict)
    pillars["profit_margin"] = get_profit_margin(company_overview_dict)
    pillars["profit_growth"] = get_profit_growth(income_statement_dict)
    pillars["revenue_growth"] = get_revenue_growth(income_statement_dict)
    pillars["current_assets_vs_liabilities"] = get_current_assets_vs_liabilities(balance_sheet_dict)
    pillars["total_assets_vs_liabilities"] = get_total_assets_vs_liabilities(balance_sheet_dict)
    # change in shares outstanding STOCKO-58 STOCKO-40
    # fcf growth STOCKO-60
    pillars["fcf_growth"] = get_fcf_growth(cash_flow_dict)
    # fcf evaluation STOCKO-61 STOCKO-39
    desired_price, desired_marketcap = get_fcf_evaluation(cash_flow_dict)
    pillars["fcf_desired_price"] = desired_price
    pillars["fcf_desired_marketcap"] = desired_marketcap


    return pillars
