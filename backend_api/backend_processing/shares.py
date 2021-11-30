# returns STRING of the current shares outstanding

from datetime import datetime

def get_shares_outstanding(company_overview_dict):
    
    shares_outstanding = company_overview_dict["shares_outstanding"]
    
    return shares_outstanding

def get_split_reversal(balance_sheet_dict, company_overview_dict):
    date = company_overview_dict["last_split_date"]
    factor = company_overview_dict["last_split_factor"]
    final_factor = 1
    try:
        split_date = datetime.fromisoformat(date)
        history_date = datetime.fromisoformat(balance_sheet_dict["fiscalDateEnding"][4])
    except:
        print("Could not parse date : returning split factor of 1")
        return final_factor
    try:
        if split_date > history_date:
            print("MODIFY SHARES OUTSTANDING")
            try:
                factor = factor.split(':')
                factor = list(map(int, factor))
                if factor[0] == 1:
                    # print("Reversal, divide by factor[1]")
                    final_factor = 1 / factor[1]
                elif factor[1] == 1:
                    # print("Split, multiply by factor [0]")
                    final_factor = factor[0]
                else:
                    print("Split/Reversal issue")
            except:
                print("Split/Reversal issue!!!")
        elif split_date < history_date:
            print("DONT MODIFY SHARES OUTSTANDING")
        else:
            print("ERROR WITH DATES")
    except:
        print("ERROR WITH DATES!!!")

    return final_factor

# returns STRING of the 5 year change in shares outstanding
def get_share_change(balance_sheet_dict, company_overview_dict):
    print(balance_sheet_dict["commonStockSharesOutstanding"])
    
    # factor = get_split_reversal(balance_sheet_dict, company_overview_dict)
    factor = 1
    current_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][0])
    five_years_ago_shares = (factor * int(balance_sheet_dict["commonStockSharesOutstanding"][4]))
    change_in_shares_outstanding = 100 * (current_shares - five_years_ago_shares) / five_years_ago_shares
    change_in_shares_outstanding = "{:.2f}".format(change_in_shares_outstanding)
    return str(change_in_shares_outstanding)

# similar as the above reversal function but can be used in an interative manner
def get_split_reversal_logic(balance_sheet_dict, company_overview_dict, x):
    date = company_overview_dict["last_split_date"]
    factor = company_overview_dict["last_split_factor"]
    final_factor = 1
    try:
        split_date = datetime.fromisoformat(date)
        history_date = datetime.fromisoformat(balance_sheet_dict["fiscalDateEnding"][x+1])
        current_date = datetime.fromisoformat(balance_sheet_dict["fiscalDateEnding"][x])
        print(split_date)
        print(history_date)
    except:
        print("Could not parse date : returning split factor of 1")
        return final_factor
    try:
        if split_date > history_date and split_date < current_date:
            print("MODIFY SHARES OUTSTANDING")
            try:
                factor = factor.split(':')
                factor = list(map(int, factor))
                if factor[0] == 1:
                    # print("Reversal, divide by factor[1]")
                    final_factor = 1 / factor[1]
                elif factor[1] == 1:
                    # print("Split, multiply by factor [0]")
                    final_factor = factor[0]
                else:
                    print("Split/Reversal issue")
            except:
                print("Split/Reversal issue!!!")
        elif split_date < history_date:
            print("DONT MODIFY SHARES OUTSTANDING")
        else:
            print("ERROR WITH DATES")
    except:
        print("ERROR WITH DATES!!!")

    return final_factor

# returns STRING of the 5 year change avg in shares outstanding
def get_share_change_avg(balance_sheet_dict, company_overview_dict):
    sum = 0
    for x in range(4):
        # factor = get_split_reversal_logic(balance_sheet_dict, company_overview_dict, x)
        factor = 1
        # print("THIS IS THE CALC FACTOR: ", factor)
        current_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][x])
        previous_shares = (factor * int(balance_sheet_dict["commonStockSharesOutstanding"][x+1]))
        change = (current_shares - previous_shares) / previous_shares
        sum = sum + change
    change_avg = 100 * sum /4
    change_avg = "{:.2f}".format(change_avg)
    return str(change_avg)