import yfinance as yahooFinance

GetCompanyInformation = yahooFinance.Ticker('XOM')
print(GetCompanyInformation.info)