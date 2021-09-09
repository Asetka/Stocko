# pillar evaluations

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

def get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    pillars = {}
    pillars["pe_ratio"] = get_pe(company_overview_dict)
    pillars["profit_margin"] = get_profit_margin(company_overview_dict)
    pillars["profit_growth"] = get_profit_growth(income_statement_dict)
    pillars["revenue_growth"] = get_revenue_growth(income_statement_dict)



    return pillars
