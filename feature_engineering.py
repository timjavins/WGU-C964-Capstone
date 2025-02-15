import pandas as pd

def create_features(data):
    data['Return'] = data['Close'].pct_change()
    data['Volatility'] = data['Return'].rolling(window=21).std()
    data['Momentum'] = data['Close'].rolling(window=21).mean()
    data = data.dropna()
    return data

if __name__ == "__main__":
    file_path = "AAPL_data_preprocessed.csv"
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    data = create_features(data)
    data.to_csv("AAPL_data_features.csv")
