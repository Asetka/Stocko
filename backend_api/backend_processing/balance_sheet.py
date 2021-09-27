# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the balance sheet api request

import requests

def get_balance_sheet(ticker, api_urls):
    
    req = requests.get(api_urls["balance_sheet_url"])
    response = req.json()
    annual_reports = response["annualReports"]

    balance_sheet_dict = {}
    reportedCurrency = []
    fiscalDateEnding = []
    totalAssets = []
    totalCurrentAssets = []
    cashAndCashEquivalentsAtCarryingValue = []
    cashAndShortTermInvestments = []
    inventory = []
    currentNetReceivables = []
    totalNonCurrentAssets = []
    propertyPlantEquipment = []
    accumulatedDepreciationAmortizationPPE = []
    intangibleAssets = []
    intangibleAssetsExcludingGoodwill = []
    goodwill = []
    investments = []
    longTermInvestments = []
    shortTermInvestments = []
    otherNonCurrrentAssets = []
    otherCurrentAssets = []
    totalLiabilities = []
    totalCurrentLiabilities = []
    currentAccountsPayable = []
    deferredRevenue = []
    currentDebt = []
    shortTermDebt = []
    totalNonCurrentLiabilities = []
    capitalLeaseObligations = []
    longTermDebt = []
    currentLongTermDebt = []
    longTermDebtNoncurrent = []
    shortLongTermDebtTotal = []
    otherCurrentLiabilities = []
    otherNonCurrentLiabilities = []
    totalShareholderEquity = []
    treasuryStock = []
    retainedEarnings = []
    commonStock = []
    commonStockSharesOutstanding = []

    for fiscal_report in annual_reports:
        reportedCurrency.append(fiscal_report["reportedCurrency"])
        fiscalDateEnding.append(fiscal_report["fiscalDateEnding"])
        totalAssets.append(fiscal_report["totalAssets"])
        totalCurrentAssets.append(fiscal_report["totalCurrentAssets"])
        cashAndCashEquivalentsAtCarryingValue.append(fiscal_report["cashAndCashEquivalentsAtCarryingValue"])
        cashAndShortTermInvestments.append(fiscal_report["cashAndShortTermInvestments"])
        inventory.append(fiscal_report["inventory"])
        currentNetReceivables.append(fiscal_report["currentNetReceivables"])
        totalNonCurrentAssets.append(fiscal_report["totalNonCurrentAssets"])
        propertyPlantEquipment.append(fiscal_report["propertyPlantEquipment"])
        accumulatedDepreciationAmortizationPPE.append(fiscal_report["accumulatedDepreciationAmortizationPPE"])
        intangibleAssets.append(fiscal_report["intangibleAssets"])
        intangibleAssetsExcludingGoodwill.append(fiscal_report["intangibleAssetsExcludingGoodwill"])
        goodwill.append(fiscal_report["goodwill"])
        investments.append(fiscal_report["investments"])
        longTermInvestments.append(fiscal_report["longTermInvestments"])
        shortTermInvestments.append(fiscal_report["shortTermInvestments"])
        otherNonCurrrentAssets.append(fiscal_report["otherNonCurrrentAssets"])
        otherCurrentAssets.append(fiscal_report["otherCurrentAssets"])
        totalLiabilities.append(fiscal_report["totalLiabilities"])
        totalCurrentLiabilities.append(fiscal_report["totalCurrentLiabilities"])
        currentAccountsPayable.append(fiscal_report["currentAccountsPayable"])
        deferredRevenue.append(fiscal_report["deferredRevenue"])
        currentDebt.append(fiscal_report["currentDebt"])
        shortTermDebt.append(fiscal_report["shortTermDebt"])
        totalNonCurrentLiabilities.append(fiscal_report["totalNonCurrentLiabilities"])
        capitalLeaseObligations.append(fiscal_report["capitalLeaseObligations"])
        longTermDebt.append(fiscal_report["longTermDebt"])
        currentLongTermDebt.append(fiscal_report["currentLongTermDebt"])
        longTermDebtNoncurrent.append(fiscal_report["longTermDebtNoncurrent"])
        shortLongTermDebtTotal.append(fiscal_report["shortLongTermDebtTotal"])
        otherCurrentLiabilities.append(fiscal_report["otherCurrentLiabilities"])
        otherNonCurrentLiabilities.append(fiscal_report["otherNonCurrentLiabilities"])
        totalShareholderEquity.append(fiscal_report["totalShareholderEquity"])
        treasuryStock.append(fiscal_report["treasuryStock"])
        retainedEarnings.append(fiscal_report["retainedEarnings"])
        commonStock.append(fiscal_report["commonStock"])
        commonStockSharesOutstanding.append(fiscal_report["commonStockSharesOutstanding"])

    balance_sheet_dict["reportedCurrency"] = reportedCurrency
    balance_sheet_dict["fiscalDateEnding"] = fiscalDateEnding
    balance_sheet_dict["totalAssets"] = totalAssets
    balance_sheet_dict["totalCurrentAssets"] = totalCurrentAssets
    balance_sheet_dict["cashAndCashEquivalentsAtCarryingValue"] = cashAndCashEquivalentsAtCarryingValue
    balance_sheet_dict["cashAndShortTermInvestments"] = cashAndShortTermInvestments
    balance_sheet_dict["inventory"] = inventory
    balance_sheet_dict["currentNetReceivables"] = currentNetReceivables
    balance_sheet_dict["totalNonCurrentAssets"] = totalNonCurrentAssets
    balance_sheet_dict["propertyPlantEquipment"] = propertyPlantEquipment
    balance_sheet_dict["accumulatedDepreciationAmortizationPPE"] = accumulatedDepreciationAmortizationPPE
    balance_sheet_dict["intangibleAssets"] = intangibleAssets
    balance_sheet_dict["intangibleAssetsExcludingGoodwill"] = intangibleAssetsExcludingGoodwill
    balance_sheet_dict["goodwill"] = goodwill
    balance_sheet_dict["investments"] = investments
    balance_sheet_dict["longTermInvestments"] = longTermInvestments
    balance_sheet_dict["shortTermInvestments"] = shortTermInvestments
    balance_sheet_dict["otherNonCurrrentAssets"] = otherNonCurrrentAssets
    balance_sheet_dict["otherCurrentAssets"] = otherCurrentAssets
    balance_sheet_dict["totalLiabilities"] = totalLiabilities
    balance_sheet_dict["totalCurrentLiabilities"] = totalCurrentLiabilities
    balance_sheet_dict["currentAccountsPayable"] = currentAccountsPayable
    balance_sheet_dict["deferredRevenue"] = deferredRevenue
    balance_sheet_dict["currentDebt"] = currentDebt
    balance_sheet_dict["shortTermDebt"] = shortTermDebt
    balance_sheet_dict["totalNonCurrentLiabilities"] = totalNonCurrentLiabilities
    balance_sheet_dict["capitalLeaseObligations"] = capitalLeaseObligations
    balance_sheet_dict["longTermDebt"] = longTermDebt
    balance_sheet_dict["currentLongTermDebt"] = currentLongTermDebt
    balance_sheet_dict["longTermDebtNoncurrent"] = longTermDebtNoncurrent
    balance_sheet_dict["shortLongTermDebtTotal"] = shortLongTermDebtTotal
    balance_sheet_dict["otherCurrentLiabilities"] = otherCurrentLiabilities
    balance_sheet_dict["otherNonCurrentLiabilities"] = otherNonCurrentLiabilities
    balance_sheet_dict["totalShareholderEquity"] = totalShareholderEquity
    balance_sheet_dict["treasuryStock"] = treasuryStock
    balance_sheet_dict["retainedEarnings"] = retainedEarnings
    balance_sheet_dict["commonStock"] = commonStock
    balance_sheet_dict["commonStockSharesOutstanding"] = commonStockSharesOutstanding

    return balance_sheet_dict