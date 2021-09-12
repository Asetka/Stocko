# used for fcf evaluations

# returns avg fcf for the last 5 years
def get_avg_fcf(cash_flow_dict):
    avg_fcf = 0
    for i in range(5):
        years_fcf = int(cash_flow_dict["operatingCashflow"][i]) - int(cash_flow_dict["capitalExpenditures"][i])
        avg_fcf = avg_fcf + years_fcf
    avg_fcf = avg_fcf/5
    return avg_fcf

# returns 
def get_fcf_evaluation(cash_flow_dict):
    desired_price = -1000
    desired_marketcap = -1000
    avg_fcf = get_avg_fcf(cash_flow_dict)




    return str(desired_price), str(desired_marketcap)
