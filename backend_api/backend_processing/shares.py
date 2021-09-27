# returns STRING of the current shares outstanding

def get_shares_outstanding(company_overview_dict):
    
    shares_outstanding = company_overview_dict["shares_outstanding"]
    
    return shares_outstanding