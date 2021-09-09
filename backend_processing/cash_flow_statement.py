# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the cash flow statement api request

import requests

def get_cash_flow_statement(ticker, api_urls):
    
    req = requests.get(api_urls["cash_flow_url"])
    response = req.json()
    annual_reports = response["annualReports"]

    cash_flow_dict = {}
    fiscalDateEnding = []
    reportedCurrency = []
    operatingCashflow = []
    paymentsForOperatingActivities = []
    proceedsFromOperatingActivities = []
    changeInOperatingLiabilities = []
    changeInOperatingAssets = []
    depreciationDepletionAndAmortization = []
    capitalExpenditures = []
    changeInReceivables = []
    changeInInventory = []
    profitLoss = []
    cashflowFromInvestment = []
    cashflowFromFinancing = []
    proceedsFromRepaymentsOfShortTermDebt = []
    paymentsForRepurchaseOfCommonStock = []
    paymentsForRepurchaseOfEquity = []
    paymentsForRepurchaseOfPreferredStock = []
    dividendPayout = []
    dividendPayoutCommonStock = []
    dividendPayoutPreferredStock = []
    proceedsFromIssuanceOfCommonStock = []
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = []
    proceedsFromIssuanceOfPreferredStock = []
    proceedsFromRepurchaseOfEquity = []
    proceedsFromSaleOfTreasuryStock = []
    changeInCashAndCashEquivalents = []
    changeInExchangeRate = []
    netIncome = []

    for cash_flow_report in annual_reports:
        fiscalDateEnding.append(cash_flow_report["fiscalDateEnding"])
        reportedCurrency.append(cash_flow_report["reportedCurrency"])
        operatingCashflow.append(cash_flow_report["operatingCashflow"])
        paymentsForOperatingActivities.append(cash_flow_report["paymentsForOperatingActivities"])
        proceedsFromOperatingActivities.append(cash_flow_report["proceedsFromOperatingActivities"])
        changeInOperatingLiabilities.append(cash_flow_report["changeInOperatingLiabilities"])
        changeInOperatingAssets.append(cash_flow_report["changeInOperatingAssets"])
        depreciationDepletionAndAmortization.append(cash_flow_report["depreciationDepletionAndAmortization"])
        capitalExpenditures.append(cash_flow_report["capitalExpenditures"])
        changeInReceivables.append(cash_flow_report["changeInReceivables"])
        changeInInventory.append(cash_flow_report["changeInInventory"])
        profitLoss.append(cash_flow_report["profitLoss"])
        cashflowFromInvestment.append(cash_flow_report["cashflowFromInvestment"])
        cashflowFromFinancing.append(cash_flow_report["cashflowFromFinancing"])
        proceedsFromRepaymentsOfShortTermDebt.append(cash_flow_report["proceedsFromRepaymentsOfShortTermDebt"])
        paymentsForRepurchaseOfCommonStock.append(cash_flow_report["paymentsForRepurchaseOfCommonStock"])
        paymentsForRepurchaseOfEquity.append(cash_flow_report["paymentsForRepurchaseOfEquity"])
        paymentsForRepurchaseOfPreferredStock.append(cash_flow_report["paymentsForRepurchaseOfPreferredStock"])
        dividendPayout.append(cash_flow_report["dividendPayout"])
        dividendPayoutCommonStock.append(cash_flow_report["dividendPayoutCommonStock"])
        dividendPayoutPreferredStock.append(cash_flow_report["dividendPayoutPreferredStock"])
        proceedsFromIssuanceOfCommonStock.append(cash_flow_report["proceedsFromIssuanceOfCommonStock"])
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet.append(cash_flow_report["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"])
        proceedsFromIssuanceOfPreferredStock.append(cash_flow_report["proceedsFromIssuanceOfPreferredStock"])
        proceedsFromRepurchaseOfEquity.append(cash_flow_report["proceedsFromRepurchaseOfEquity"])
        proceedsFromSaleOfTreasuryStock.append(cash_flow_report["proceedsFromSaleOfTreasuryStock"])
        changeInCashAndCashEquivalents.append(cash_flow_report["changeInCashAndCashEquivalents"])
        changeInExchangeRate.append(cash_flow_report["changeInExchangeRate"])
        netIncome.append(cash_flow_report["netIncome"])

    cash_flow_dict["fiscalDateEnding"] = fiscalDateEnding
    cash_flow_dict["reportedCurrency"] = reportedCurrency
    cash_flow_dict["operatingCashflow"] = operatingCashflow
    cash_flow_dict["paymentsForOperatingActivities"] = paymentsForOperatingActivities
    cash_flow_dict["proceedsFromOperatingActivities"] = proceedsFromOperatingActivities
    cash_flow_dict["changeInOperatingLiabilities"] = changeInOperatingLiabilities
    cash_flow_dict["changeInOperatingAssets"] = changeInOperatingAssets
    cash_flow_dict["depreciationDepletionAndAmortization"] = depreciationDepletionAndAmortization
    cash_flow_dict["capitalExpenditures"] = capitalExpenditures
    cash_flow_dict["changeInReceivables"] = changeInReceivables
    cash_flow_dict["changeInInventory"] = changeInInventory
    cash_flow_dict["profitLoss"] = profitLoss
    cash_flow_dict["cashflowFromInvestment"] = cashflowFromInvestment
    cash_flow_dict["cashflowFromFinancing"] = cashflowFromFinancing
    cash_flow_dict["proceedsFromRepaymentsOfShortTermDebt"] = proceedsFromRepaymentsOfShortTermDebt
    cash_flow_dict["paymentsForRepurchaseOfCommonStock"] = paymentsForRepurchaseOfCommonStock
    cash_flow_dict["paymentsForRepurchaseOfEquity"] = paymentsForRepurchaseOfEquity
    cash_flow_dict["paymentsForRepurchaseOfPreferredStock"] = paymentsForRepurchaseOfPreferredStock
    cash_flow_dict["dividendPayout"] = dividendPayout
    cash_flow_dict["dividendPayoutCommonStock"] = dividendPayoutCommonStock
    cash_flow_dict["dividendPayoutPreferredStock"] = dividendPayoutPreferredStock
    cash_flow_dict["proceedsFromIssuanceOfCommonStock"] = proceedsFromIssuanceOfCommonStock
    cash_flow_dict["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"] = proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet
    cash_flow_dict["proceedsFromIssuanceOfPreferredStock"] = proceedsFromIssuanceOfPreferredStock
    cash_flow_dict["proceedsFromRepurchaseOfEquity"] = proceedsFromRepurchaseOfEquity
    cash_flow_dict["proceedsFromSaleOfTreasuryStock"] = proceedsFromSaleOfTreasuryStock
    cash_flow_dict["changeInCashAndCashEquivalents"] = changeInCashAndCashEquivalents
    cash_flow_dict["changeInExchangeRate"] = changeInExchangeRate
    cash_flow_dict["netIncome"] = netIncome

    return cash_flow_dict