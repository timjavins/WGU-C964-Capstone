import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

if __name__ == "__main__":
    file_path = "AAPL_data.csv"
    data = preprocess_data(file_path)
    data.to_csv("AAPL_data_preprocessed.csv")
