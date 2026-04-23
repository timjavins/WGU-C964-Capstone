import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import yfinance as yf

# def download_stock_data(ticker, start_date, end_date):
#     stock_data = yf.download(ticker, start=start_date, end=end_date)
#     return stock_data

ticker = "AAPL"
start_date = "2010-01-01"
end_date = "2024-01-01"


def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()
    data = data.rename(columns={'Price': 'Date'})
    # Delete rows 1 and 3
    data = data.drop(data.index[[0, 1]])
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    for col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    return data

file_path = "AAPL_data.csv"
data = preprocess_data(file_path)
data.to_csv("AAPL_data_preprocessed.csv")

def create_features(data):
    data['Return'] = data['Close'].pct_change()
    data['Volatility'] = data['Return'].rolling(window=21).std()
    data['Momentum'] = data['Close'].rolling(window=21).mean()
    data = data.dropna()
    return data

file_path = "AAPL_data_preprocessed.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
data = create_features(data)
data.to_csv("AAPL_data_features.csv")


def train_model(data):
    data['Target_Return'] = data['Return'].shift(-1) # shift target to have tomorrow's return as the label
    data = data.dropna()  # drop the last row where Target_Return is NaN
    X = data[['Volatility', 'Momentum']]
    y = data['Target_Return']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=1000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model

file_path = "AAPL_data_features.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
model = train_model(data)
model.save_model("1yo_xgboost_model.json")

def evaluate_model(model, data):
    X = data[['Volatility', 'Momentum']]
    y = data['Return']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error: {mse}")

file_path = "AAPL_data_features.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
model = xgb.XGBRegressor()
model.load_model("1yo_xgboost_model.json")
evaluate_model(model, data)

def implement_strategy(model, data):
    # Get prediction for tomorrow's return using today's data
    data['Predicted_Return'] = model.predict(data[['Volatility', 'Momentum']])
    data['Signal'] = data['Predicted_Return'].apply(lambda x: 1 if x > 0 else -1)
    # Align the signal with tomorrow's actual return
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Return']
    data = data.dropna()
    return data

file_path = "AAPL_data_features.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
model = xgb.XGBRegressor()
model.load_model("1yo_xgboost_model.json")
data = implement_strategy(model, data)
data.to_csv("AAPL_strategy.csv")

def backtest_strategy(data):
    data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()
    data['Cumulative_Market_Return'] = (1 + data['Return']).cumprod()
    return data

file_path = "AAPL_strategy.csv"
data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
data = backtest_strategy(data)
data.to_csv("AAPL_backtest.csv")

def test_model(model, data):
    X = data[['Volatility', 'Momentum']]
    y = data['Return']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error on unseen data: {mse}")

# Download new stock data
ticker = "AAPL"
start_date = "2024-01-01"
end_date = "2025-01-31"
# new_data = download_stock_data(ticker, start_date, end_date)
# new_data.to_csv(f"{ticker}_new_data.csv")

# Preprocess the new stock data
prep_data = preprocess_data(f"{ticker}_new_data.csv")

# Create new features for the new stock data
new_features = create_features(prep_data)
new_features.to_csv(f"{ticker}_new_data_features.csv")

# Test the model on the new data
test_model(model, new_features)

# Save the test results to CSV
new_features.to_csv(f"{ticker}_new_data_with_predictions.csv")

# Implement the strategy on the new data
model_and_signals = implement_strategy(model, new_features)
model_and_signals.to_csv(f"{ticker}_new_data_with_signals.csv")

# Get S&P 500 data for 2020 through 2024
# sp500_data = yf.download("^GSPC", start="2024-01-01", end="2025-01-31")
# sp500_data.to_csv("SP500_data.csv")

# Preprocess the S&P 500 data
sp500_data = preprocess_data("SP500_data.csv")
sp500_data.to_csv("SP500_data_preprocessed.csv")

# Create features for the S&P 500 data
sp500_features = create_features(sp500_data)
sp500_features.to_csv("SP500_data_features.csv")

# Compare the gains of the trading strategy vs. the S&P 500
model_and_signals = pd.read_csv(f"{ticker}_new_data_with_signals.csv", index_col='Date', parse_dates=True)
sp500_features = pd.read_csv("SP500_data_features.csv", index_col='Date', parse_dates=True)

# Add missing columns to the S&P 500 data
# For the buy-and-hold S&P 500, assign the daily return directly.
sp500_features['Strategy_Return'] = sp500_features['Return']

#Backtest the trading strategy and the S&P 500
model_and_signals = backtest_strategy(model_and_signals)
sp500_features = backtest_strategy(sp500_features)

model_and_signals.to_csv(f"{ticker}_new_data_with_signals_backtest.csv")
sp500_features.to_csv("SP500_data_features_backtest.csv")


plt.figure(figsize=(12, 6))
plt.plot(model_and_signals['Cumulative_Strategy_Return'], label=f'{ticker} Trading Strategy')
plt.plot(sp500_features['Cumulative_Market_Return'], label='S&P 500')
plt.legend()
plt.title(f'Cumulative Returns of {ticker} Trading Strategy vs. S&P 500')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid()
plt.show()

# Plot the cumulative strategy return and market return
plt.figure(figsize=(12, 6))
plt.plot(model_and_signals['Cumulative_Strategy_Return'], label=f'{ticker} Cumulative Strategy Return')
plt.plot(model_and_signals['Cumulative_Market_Return'], label='Cumulative Market Return')
plt.legend()
plt.title('Cumulative Strategy Return vs. Cumulative Market Return')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid()
plt.show()