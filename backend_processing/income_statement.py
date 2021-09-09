# returns a DICTIONARY of keys -> lists containing 
# the last 5 years of annual data from the income statement api request

import requests

def get_income_statement(ticker, api_urls):
    
    req = requests.get(api_urls["income_statement_url"])
    response = req.json()
    annual_reports = response["annualReports"]

    income_statement_dict = {}
    fiscalDateEnding = []
    reportedCurrency = []
    grossProfit = []
    totalRevenue = []
    costOfRevenue = []
    costofGoodsAndServicesSold = []
    operatingIncome = []
    sellingGeneralAndAdministrative = []
    researchAndDevelopment = []
    operatingExpenses = []
    investmentIncomeNet = []
    netInterestIncome = []
    interestIncome = []
    interestExpense = []
    nonInterestIncome = []
    otherNonOperatingIncome = []
    depreciation = []
    depreciationAndAmortization = []
    incomeBeforeTax = []
    incomeTaxExpense = []
    interestAndDebtExpense = []
    netIncomeFromContinuingOperations = []
    comprehensiveIncomeNetOfTax = []
    ebit = []
    ebitda = []
    netIncome = []
    
    for income_report in annual_reports:
        fiscalDateEnding.append(income_report["fiscalDateEnding"])
        reportedCurrency.append(income_report["reportedCurrency"])
        grossProfit.append(income_report["grossProfit"])
        totalRevenue.append(income_report["totalRevenue"])
        costOfRevenue.append(income_report["costOfRevenue"])
        costofGoodsAndServicesSold.append(income_report["costofGoodsAndServicesSold"])
        operatingIncome.append(income_report["operatingIncome"])
        sellingGeneralAndAdministrative.append(income_report["sellingGeneralAndAdministrative"])
        researchAndDevelopment.append(income_report["researchAndDevelopment"])
        operatingExpenses.append(income_report["operatingExpenses"])
        investmentIncomeNet.append(income_report["investmentIncomeNet"])
        netInterestIncome.append(income_report["netInterestIncome"])
        interestIncome.append(income_report["interestIncome"])
        interestExpense.append(income_report["interestExpense"])
        nonInterestIncome.append(income_report["nonInterestIncome"])
        otherNonOperatingIncome.append(income_report["otherNonOperatingIncome"])
        depreciation.append(income_report["depreciation"])
        depreciationAndAmortization.append(income_report["depreciationAndAmortization"])
        incomeBeforeTax.append(income_report["incomeBeforeTax"])
        incomeTaxExpense.append(income_report["incomeTaxExpense"])
        interestAndDebtExpense.append(income_report["interestAndDebtExpense"])
        netIncomeFromContinuingOperations.append(income_report["netIncomeFromContinuingOperations"])
        comprehensiveIncomeNetOfTax.append(income_report["comprehensiveIncomeNetOfTax"])
        ebit.append(income_report["ebit"])
        ebitda.append(income_report["ebitda"])
        netIncome.append(income_report["netIncome"])

    income_statement_dict["fiscalDateEnding"] = fiscalDateEnding
    income_statement_dict["reportedCurrency"] = reportedCurrency
    income_statement_dict["grossProfit"] = grossProfit
    income_statement_dict["totalRevenue"] = totalRevenue
    income_statement_dict["costOfRevenue"] = costOfRevenue
    income_statement_dict["costofGoodsAndServicesSold"] = costofGoodsAndServicesSold
    income_statement_dict["operatingIncome"] = operatingIncome
    income_statement_dict["sellingGeneralAndAdministrative"] = sellingGeneralAndAdministrative
    income_statement_dict["researchAndDevelopment"] = researchAndDevelopment
    income_statement_dict["operatingExpenses"] = operatingExpenses
    income_statement_dict["investmentIncomeNet"] = investmentIncomeNet
    income_statement_dict["netInterestIncome"] = netInterestIncome
    income_statement_dict["interestIncome"] = interestIncome
    income_statement_dict["interestExpense"] = interestExpense
    income_statement_dict["nonInterestIncome"] = nonInterestIncome
    income_statement_dict["otherNonOperatingIncome"] = otherNonOperatingIncome
    income_statement_dict["depreciation"] = depreciation
    income_statement_dict["depreciationAndAmortization"] = depreciationAndAmortization
    income_statement_dict["incomeBeforeTax"] = incomeBeforeTax
    income_statement_dict["incomeTaxExpense"] = incomeTaxExpense
    income_statement_dict["interestAndDebtExpense"] = interestAndDebtExpense
    income_statement_dict["netIncomeFromContinuingOperations"] = netIncomeFromContinuingOperations
    income_statement_dict["comprehensiveIncomeNetOfTax"] = comprehensiveIncomeNetOfTax
    income_statement_dict["ebit"] = ebit
    income_statement_dict["ebitda"] = ebitda
    income_statement_dict["netIncome"] = netIncome
    
    return income_statement_dict