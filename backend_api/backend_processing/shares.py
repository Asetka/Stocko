# returns STRING of the current shares outstanding

def get_shares_outstanding(company_overview_dict):
    
    shares_outstanding = company_overview_dict["shares_outstanding"]
    
    return shares_outstanding



def get_split_reversal_date(company_overview_dict):
    date = company_overview_dict["last_split_date"]
    factor = company_overview_dict["last_split_factor"]
    print(date)
    print(factor)
    factor = factor.split(':')
    factor = list(map(int, factor))
    print(factor)
    try:
        if factor[0] == 1:
            print("Reversal, divide by factor[1]")
        elif factor[1] == 1:
            print("Split, multiply by factor [0]")
        else:
            print("Split/Reversal issue")
    except:
        print("Split/Reversal issue!!!")

    return date, factor



# returns STRING of the 5 year change in shares outstanding
def get_share_change(balance_sheet_dict, company_overview_dict):
    date, factor = get_split_reversal_date(company_overview_dict)
    print("Date: " + date)

    current_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][0]) / 1000000000
    five_years_ago_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][4]) / 1000000000
    print(current_shares)
    print(five_years_ago_shares)
    change_in_shares_outstanding = current_shares - five_years_ago_shares
    print("CHANGE" + str(change_in_shares_outstanding))
    # return str(change_in_shares_outstanding)