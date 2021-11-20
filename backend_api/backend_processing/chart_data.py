# returns a DICTIONARY of keys -> lists containing 
# up to the last 20 years of closing weekly price of a stock api request

import requests


def get_chart_data(ticker, api_urls):
    req = requests.get(api_urls["chart_data"])
    response = req.json()
    weekly_reports = response["Weekly Adjusted Time Series"]

    chart_data_dict = {}
    week_ending = []
    end_of_week_price = []
    start_of_week_price = []
    high_of_week_price = []
    low_of_week_price = []
    volume_of_week = []


    for key in weekly_reports:
        week_ending.append(key)
        start_of_week_price.append(weekly_reports[key]["1. open"])
        high_of_week_price.append(weekly_reports[key]["2. high"])
        low_of_week_price.append(weekly_reports[key]["3. low"])
        end_of_week_price.append(weekly_reports[key]["4. close"])
        volume_of_week.append(weekly_reports[key]["6. volume"])

    chart_data_dict["week_ending"] = week_ending
    chart_data_dict["start_of_week_price"] = start_of_week_price
    chart_data_dict["high_of_week_price"] = high_of_week_price
    chart_data_dict["low_of_week_price"] = low_of_week_price
    chart_data_dict["end_of_week_price"] = end_of_week_price
    chart_data_dict["volume_of_week"] = _of_week

    return chart_data_dict