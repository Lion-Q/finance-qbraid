import matplotlib.pyplot as plt
import datetime
from qiskit_finance.data_providers import YahooDataProvider, RandomDataProvider, WikipediaDataProvider

'''
Sample Run:
data = load_data(YahooDataProvider)
if data is not None:
    data.run()
    plot_data(data)

Can customize stocks:
data = load_data(YahooDataProvider, stocks=['AAPL', 'MSFT])
'''

def load_data(model, y1=2023, m1=1, d1=1, y2=2023, m2=12, d2=31, stocks=None, num_assets=25):
    """Return data loaded by the given model for the specified time period.
    
    @param: model The model to use
    @param: y1, m1, d1 Start date (set to 2023/01/01 by default)
    @param: y2, m2, d2 End date (set to 2023/12/31 by default)
    @param: num_assets Optional num of stock tickers to load; defaults to 25
    @param: stocks Optional list of stock tickers to load; defaults to a predefined list

    Returns None if there is an error.
    """
    try:
        data = None
        start = datetime.datetime(y1, m1, d1)
        end = datetime.datetime(y2, m2, d2)

        if model == RandomDataProvider:
            stocks = [("STOCK%s" % i) for i in range(num_assets)]
            seed = 479
            data = RandomDataProvider(tickers=stocks, start=start, end=end, seed=seed)
            return data
        else:
            if stocks is None: # Set Default Stock
                stocks = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'META', 'BRK-B',
                          'LLY', 'AVGO', 'TSLA', 'WMT', 'JPM', 'UNH', 'XOM', 'V', 'ORCL',
                          'MA', 'PG', 'COST', 'HD', 'JNJ', 'ABBV', 'NFLX', 'KO', 'BAC']
            if model == YahooDataProvider:
                data = YahooDataProvider(tickers=stocks, start=start, end=end)
                return data
            elif model == WikipediaDataProvider:
                token = "rxRPKx-ezz5A4y9c9GRG"
                data = WikipediaDataProvider(
                    token=token,
                    tickers=stocks,
                    start=start,
                    end=end,
                )
                return data

        print("Unsupported model")
        return data

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def plot_data(data):
    """Plot the given data.
    
    @param: data The data to plot (should be in the format provided by the data provider).
    """
    plt.figure(figsize=(12, 6))
    
    # Plot the data for each stock ticker
    for (cnt, s) in enumerate(data._tickers):
        plt.plot(data._data[cnt], label=s)
    
    # Customize the plot appearance
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1), ncol=1, fontsize='small')
    plt.title("Stock Prices", fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()