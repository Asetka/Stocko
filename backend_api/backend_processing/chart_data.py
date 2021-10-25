



import requests


def get_chart_data(ticker, api_urls):
    req = requests.get(api_urls["chart_data"])
    response = req.json()
    weekly_reports = response["Weekly Adjusted Time Series"]

    chart_data_dict = {}
    week_ending = []
    end_of_week_price = []

    # print(weekly_reports)
    # print(type(weekly_reports))

    for key in weekly_reports:
        week_ending.append(key)
        # print(key)
        # print(week_ending[key])
        # print()
        end_of_week_price.append(weekly_reports[key]["4. close"])

    chart_data_dict["week_ending"] = week_ending
    chart_data_dict["end_of_week_price"] = end_of_week_price

    return chart_data_dict