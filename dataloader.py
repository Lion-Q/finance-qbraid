from qiskit_finance.data_providers import YahooDataProvider

def yahooData25(y1=2023, m1=1, d1=1, y2=2024, m2=1, d2=1):
    stocks = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'META', 'BRK-B', 'LLY', 'AVGO', 'TSLA', 'WMT', 'JPM', 'UNH', 'XOM', 'V', 'ORCL', 'MA', 'PG', 'COST', 'HD', 'JNJ', 'ABBV', 'NFLX', 'KO', 'BAC']
    data = YahooDataProvider(tickers=stocks,
                     start=datetime.datetime(y1,m1,d1),
                     end=datetime.datetime(y2,m2,d2))
    data.run()
    return data
