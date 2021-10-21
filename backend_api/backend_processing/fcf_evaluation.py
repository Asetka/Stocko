# used for fcf share price evaluation

from .shares import get_shares_outstanding

# returns avg fcf for the last 5 years
def get_avg_fcf(cash_flow_dict):
    avg_fcf = 0
    for i in range(5):
        years_fcf = int(cash_flow_dict["operatingCashflow"][i]) - int(cash_flow_dict["capitalExpenditures"][i])
        avg_fcf = avg_fcf + years_fcf
    avg_fcf = avg_fcf/5
    return avg_fcf

# returns 
def get_fcf_evaluation(cash_flow_dict, company_overview_dict):
    desired_price = -1000
    desired_marketcap = -1000
    avg_fcf = get_avg_fcf(cash_flow_dict)
    # print(avg_fcf)

    # desired_pe = input("What is your PE for this company: ")
    desired_pe = 20
    print()
    # print(desired_pe)

    shares_outstanding = get_shares_outstanding(company_overview_dict)
    desired_marketcap = avg_fcf * int(desired_pe)
    desired_marketcap = "{:,.0f}".format(desired_marketcap)
    desired_price = int(desired_marketcap) / int(shares_outstanding)
    desired_price = "{:,.2f}".format(desired_price)
    return str(desired_price), str(desired_marketcap)
