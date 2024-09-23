import numpy as np
import pandas as pd
import yfinance as yf

# Download historical data for top 30 stocks on S&P 500 (not including BRK.b, PEP; these ran into errors for some reason)
tickers = ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AVGO', 'GOOG', 'LLY', 'TSLA', 'JPM', 'UNH', 'XOM', 'V', 'PG', 'MA', 'COST', 'JNJ', 'HD', 'WMT', 'ABBV', 'NFLX', 'MRK', 'KO', 'BAC', 'ORCL', 'CRM', 'AMD', 'CVX', 'TMO']
data = yf.download(tickers, start="2024-01-01", end="2024-04-01")['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

returns.to_csv("SP30.csv")
