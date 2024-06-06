import yfinance as yf

tickers = ['XOM']

for ticker in tickers:
    GetCompanyInformation = yf.Ticker(ticker)
    print(ticker,end="")
    print(':',end="")
    print(GetCompanyInformation.info['returnOnEquity'])