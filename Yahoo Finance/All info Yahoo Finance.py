import yfinance as yahooFinance

tickers = [] # here you can write the tickers of the companies you need. Do not forget ''! For example, for ExxonMobil it will be 'XOM'.

for ticker in tickers:
    print(yahooFinance.Ticker(ticker).info)
