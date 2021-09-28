# returns a DICTIONARY of information to be used regarding company overview api request
import requests

def get_company_overview(ticker, api_urls):
    
    req = requests.get(api_urls["company_overview_url"])
    response = req.json()

    overview_dict = {
        "symbol" : response["Symbol"],
        "asset_type" : response["AssetType"],
        "name" : response["Name"],
        "description" : response["Description"],
        "cik" : response["CIK"],
        "exchange" : response["Exchange"],
        "currency" :response["Currency"],
        "country" : response["Country"],
        "sector" : response["Sector"],
        "industry" : response["Industry"],
        "address" : response["Address"],
        "fiscal_year_end" : response["FiscalYearEnd"],
        "latest_quarter" : response["LatestQuarter"],
        "market_cap" : response["MarketCapitalization"],
        "ebitda" : response["EBITDA"],
        "pe_ratio" : response["PERatio"],
        "peg_ratio" : response["PEGRatio"],
        "book_value" : response["BookValue"],
        "dividend_per_share" : response["DividendPerShare"],
        "dividend_yield" : response["DividendYield"],
        "eps" : response["EPS"],
        "revenue_per_share_ttm" : response["RevenuePerShareTTM"],
        "profit_margin" : response["ProfitMargin"],
        "operating_margin_ttm" : response["OperatingMarginTTM"],
        "return_on_assets_ttm" : response["ReturnOnAssetsTTM"],
        "return_on_equity_ttm" : response["ReturnOnEquityTTM"],
        "revenue_ttm" : response["RevenueTTM"],
        "gross_profit_ttm" : response["GrossProfitTTM"],
        "diluted_epsttm" : response["DilutedEPSTTM"],
        "quarterly_earnings_growth_yoy" : response["QuarterlyEarningsGrowthYOY"],
        "quarterly_revenue_growth_yoy" : response["QuarterlyRevenueGrowthYOY"],
        "analyst_target_price" : response["AnalystTargetPrice"],
        "trailing_pe" : response["TrailingPE"],
        "foward_pe" : response["ForwardPE"],
        "price_to_sales_ratio_ttm" : response["PriceToSalesRatioTTM"],
        "price_to_book_ratio" : response["PriceToBookRatio"],
        "ev_to_revenue" : response["EVToRevenue"],
        "ev_to_ebitda" : response["EVToEBITDA"],
        "beta" : response["Beta"],
        "52_week_high" : response["52WeekHigh"],
        "52_week_low" : response["52WeekLow"],
        "50_day_moving_average" : response["50DayMovingAverage"],
        "200_day_moving_average" : response["200DayMovingAverage"],
        "shares_outstanding" : response["SharesOutstanding"],
        "shares_float" : response["SharesFloat"],
        "shares_short" : response["SharesShort"],
        "shares_shot_prior_month" : response["SharesShortPriorMonth"],
        "short_ratio" : response["ShortRatio"],
        "short_precent_outstanding" : response["ShortPercentOutstanding"],
        "short_percent_float" : response["ShortPercentFloat"],
        "percent_insiders" : response["PercentInsiders"],
        "percent_institutions" : response["PercentInstitutions"],
        "foward_annual_dividend_rate" : response["ForwardAnnualDividendRate"],
        "foward_annual_dividend_yield" : response["ForwardAnnualDividendYield"],
        "payout_ratio" :  response["PayoutRatio"],
        "dividend_date" : response["DividendDate"],
        "ex_dividend_date" : response["ExDividendDate"],
        "last_split_factor" : response["LastSplitFactor"],
        "last_split_date" : response["LastSplitDate"]
    }

    return overview_dict