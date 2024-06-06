import yfinance as yf

tickers = [] # here you can write the tickers of the companies you need. Do not forget ''! For example, for ExxonMobil it will be 'XOM'.

for ticker in tickers:
    print(ticker,end="")
    print(':',end="")
    print(yf.Ticker(ticker).info['returnOnEquity'])
