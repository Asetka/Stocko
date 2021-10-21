from .shares import get_share_change
from .pillar_evaluations import get_revenue_growth
from .pillar_evaluations import get_profit_margin
from .pillar_evaluations import get_fcf_growth


def get_price_to_fcf(company_overview_dict, cash_flow_dict):
    market_cap = int(company_overview_dict["market_cap"])
    fcf = int(cash_flow_dict["operatingCashflow"][0]) - int(cash_flow_dict["capitalExpenditures"][0])
    price_fcf_ratio = market_cap / fcf
    return str(price_fcf_ratio)

def get_forecast_table(ticker, company_overview_dict, balance_sheet_dict, income_statement_dict, cash_flow_dict):
    forecast_dict = {}
    forecast_dict["revenue_growth"] = get_revenue_growth(income_statement_dict)
    forecast_dict["change_in_shares_ourstanding"] = get_share_change(balance_sheet_dict, company_overview_dict)
    forecast_dict["profit_margin"] = get_profit_margin(company_overview_dict)
    forecast_dict["fcf_growth"] = get_fcf_growth(cash_flow_dict)
    forecast_dict["pe_ratio"] = company_overview_dict["pe_ratio"]
    forecast_dict["price_to)fcf"] = get_price_to_fcf(company_overview_dict, cash_flow_dict)
    forecast_dict["Annual Return"] = "---"

    return forecast_dict