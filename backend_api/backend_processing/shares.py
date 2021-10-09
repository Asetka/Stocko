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
        if split_date >= history_date:
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
    factor = get_split_reversal(balance_sheet_dict, company_overview_dict)
    current_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][0])
    five_years_ago_shares = (factor * int(balance_sheet_dict["commonStockSharesOutstanding"][4]))
    # current_shares = int(balance_sheet_dict["commonStockSharesOutstanding"][0]) / 1000000000
    # five_years_ago_shares = (factor * int(balance_sheet_dict["commonStockSharesOutstanding"][4])) / 1000000000
    change_in_shares_outstanding = 100 * (current_shares - five_years_ago_shares) / five_years_ago_shares
    return str(change_in_shares_outstanding)