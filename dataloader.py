from qiskit_finance.data_providers import YahooDataProvider
stocks = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'META', 'BRK-B', 'LLY', 'AVGO', 'TSLA', 'WMT', 'JPM', 'UNH', 'XOM', 'V', 'ORCL', 'MA', 'PG', 'COST', 'HD', 'JNJ', 'ABBV', 'NFLX', 'KO', 'BAC']
data = YahooDataProvider(tickers=stocks,
                 start=datetime.datetime(2023,1,1),
                 end=datetime.datetime(2024,1,1))
data.run()
