import pandas as pd

def backtest_strategy(data):
    data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()
    data['Cumulative_Market_Return'] = (1 + data['Return']).cumprod()
    return data

if __name__ == "__main__":
    file_path = "AAPL_strategy.csv"
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    data = backtest_strategy(data)
    data.to_csv("AAPL_backtest.csv")
