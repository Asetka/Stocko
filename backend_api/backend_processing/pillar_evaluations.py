# pillar evaluations

from .fcf_evaluation import get_fcf_evaluation
from .shares import get_share_change

# returns STRING of the companies PE Ratio
def get_pe(company_overview_dict):
    pe_ratio = company_overview_dict["pe_ratio"]
    return pe_ratio

# returns STRING of the profit margin
def get_profit_margin(company_overview_dict):
    profit_margin = company_overview_dict["profit_margin"]
    profit_margin = float(profit_margin) * 100
    profit_margin = "{:.2f}".format(profit_margin)
    return str(profit_margin)

# returns STRING of the profit growth as a PERCENTAGE over the last 5 years
def get_profit_growth(income_statement_dict):
    current_profit = int(income_statement_dict["grossProfit"][0])
    previous_profit = int(income_statement_dict["grossProfit"][4])
    profit_growth = 100 * (current_profit - previous_profit) / previous_profit
    profit_growth = "{:.2f}".format(profit_growth)
    return str(profit_growth)

# returns STRING of the revenue growth as a PERCENTAGE over the last 5 years
def get_revenue_growth(income_statement_dict):
    current_revenue = int(income_statement_dict["totalRevenue"][0])
    previous_revenue = int(income_statement_dict["totalRevenue"][4])
    revenue_growth = 100 * (current_revenue - previous_revenue) / previous_revenue
    revenue_growth = "{:.2f}".format(revenue_growth)
    return str(revenue_growth)

# returns STRING of current assets vs liabilities
def get_current_assets_vs_liabilities(balance_sheet_dict):   
    total_current_assets_vs_liabilities = int(balance_sheet_dict["totalCurrentAssets"][0]) - int(balance_sheet_dict["totalCurrentLiabilities"][0])
    total_current_assets_vs_liabilities = "{:.0f}".format(total_current_assets_vs_liabilities)
    return str(total_current_assets_vs_liabilities)

# returns STRING of total assets vs liabilities
def get_total_assets_vs_liabilities(balance_sheet_dict):
    total_assets_vs_liabilities = int(balance_sheet_dict["totalAssets"][0]) - int(balance_sheet_dict["totalLiabilities"][0])
    total_assets_vs_liabilities = "{:.0f}".format(total_assets_vs_liabilities)
    return str(total_assets_vs_liabilities)

# returns STRING of the fcf growth as a PERCENTAGE over the last 5 years
def get_fcf_growth(cash_flow_dict):
    current_fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    previous_fcf = int(cash_flow_dict["operatingCashflow"][4]) - int(cash_flow_dict["capitalExpenditures"][4])
    fcf_growth = 100 * (current_fcf - previous_fcf) / previous_fcf
    fcf_growth = "{:.2f}".format(fcf_growth)
    return str(fcf_growth)

# returns STRING of the ev to ebitda ratio 
def get_ev_ebitda_ratio(company_overview_dict):
    ev_ebitda_ratio = company_overview_dict["ev_to_ebitda"]
    return str(ev_ebitda_ratio)

# returns STRING of the price to book ratio 
def get_price_to_book_ratio(company_overview_dict):
    price_to_book_ratio = company_overview_dict["price_to_book_ratio"]
    return str(price_to_book_ratio)


def get_pillar_evaluations(company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    pillars = {}

    # STOCKO-74
    years_of_history = len(balance_sheet_dict["reportedCurrency"])
    if years_of_history != 5:
        pillars["years_of_history_error"] = True
        return pillars

    pillars["years_of_history_error"] = False
    pillars["pe_ratio"] = get_pe(company_overview_dict)
    pillars["profit_margin"] = get_profit_margin(company_overview_dict)
    pillars["profit_growth"] = get_profit_growth(income_statement_dict)
    pillars["revenue_growth"] = get_revenue_growth(income_statement_dict)
    pillars["current_assets_vs_liabilities"] = get_current_assets_vs_liabilities(balance_sheet_dict)
    pillars["total_assets_vs_liabilities"] = get_total_assets_vs_liabilities(balance_sheet_dict)
    pillars["change_in_shares_ourstanding"] = get_share_change(balance_sheet_dict, company_overview_dict)
    # pillars["change_in_shares_ourstanding"] = "API Data Schema Changed; New Logic Will Be Implemented Shortly"
    pillars["fcf_growth"] = get_fcf_growth(cash_flow_dict)
    desired_price, desired_marketcap = get_fcf_evaluation(cash_flow_dict, company_overview_dict)
    pillars["fcf_desired_price"] = desired_price
    pillars["fcf_desired_marketcap"] = desired_marketcap
    pillars["ev_ebitda_ratio"] = get_ev_ebitda_ratio(company_overview_dict)
    pillars["price_to_book_ratio"] = get_price_to_book_ratio(company_overview_dict)


    return pillars
