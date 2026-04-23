import pandas as pd
import yfinance as yf
import xgboost as xgb
import sklearn
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Data Collection
def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

ticker = "AAPL"
start_date = "2010-01-01"
end_date = "2024-01-01"
data = download_stock_data(ticker, start_date, end_date)
data.to_csv(f"{ticker}_data.csv")

# Data Preprocessing
def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()
    data = data.rename(columns={'Price': 'Date'})
    # Delete rows 2 and 3
    data = data.drop(data.index[[0, 1]])
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    for col in data.columns:
        data[col] = pd.to_numeric(data[col])
    return data

if __name__ == "__main__":
    file_path = "AAPL_data.csv"
    data = preprocess_data(file_path)
    data.to_csv("AAPL_data_preprocessed.csv")

# Feature Engineering
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

# Model Training
def train_model(data):
    # shift target to have tomorrow's return as the label
    data['Target_Return'] = data['Return'].shift(-1)
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

# Model Evaluation
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

# Trading Strategy
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

# Backtesting
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
new_data = download_stock_data(ticker, start_date, end_date)
new_data.to_csv(f"{ticker}_new_data.csv")
print(new_data.head())

# Preprocess the new stock data
prep_data = preprocess_data(f"{ticker}_new_data.csv")

print("Prepped data")
print(prep_data.head())

# Create new features for the new stock data
new_features = create_features(prep_data)
print("New features")
print(new_features.head())
new_features.to_csv(f"{ticker}_new_data_features.csv")

# Test the model on the new data
test_model(model, new_features)

# Save the test results to CSV
new_features.to_csv(f"{ticker}_new_data_with_predictions.csv")

# Implement the strategy on the new data
model_and_signals = implement_strategy(model, new_features)
model_and_signals.to_csv(f"{ticker}_new_data_with_signals.csv")

# Get S&P 500 data for 2020 through 2024
sp500_data = yf.download("^GSPC", start="2024-01-01", end="2025-01-31")
sp500_data.to_csv("SP500_data.csv")

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

# Calculate the Sharpe ratio for the trading strategy and the S&P 500
def calculate_sharpe_ratio(data):
    returns = data['Return']
    sharpe_ratio = returns.mean() / returns.std()
    return sharpe_ratio

sharpe_ratio_model = calculate_sharpe_ratio(model_and_signals)
sharpe_ratio_sp500 = calculate_sharpe_ratio(sp500_features)

print(f"Sharpe Ratio for Trading Strategy: {sharpe_ratio_model}")
print(f"Sharpe Ratio for S&P 500: {sharpe_ratio_sp500}")

# Calculate the maximum drawdown for the trading strategy and the S&P 500
def calculate_max_drawdown(data):
    cum_returns = data['Cumulative_Strategy_Return']
    max_return = cum_returns.cummax()
    drawdown = (cum_returns - max_return) / max_return
    max_drawdown = drawdown.min()
    return max_drawdown

max_drawdown_model = calculate_max_drawdown(model_and_signals)
max_drawdown_sp500 = calculate_max_drawdown(sp500_features)

print(f"Maximum Drawdown for Trading Strategy: {max_drawdown_model}")
print(f"Maximum Drawdown for S&P 500: {max_drawdown_sp500}")

# Calculate the annualized return for the trading strategy and the S&P 500
def calculate_annualized_return(data):
    cum_return = data['Cumulative_Strategy_Return']
    start_date = cum_return.index[0]
    end_date = cum_return.index[-1]
    years = (end_date - start_date).days / 365
    annualized_return = (cum_return[-1] ** (1 / years)) - 1
    return annualized_return

annualized_return_model = calculate_annualized_return(model_and_signals)
annualized_return_sp500 = calculate_annualized_return(sp500_features)

print(f"Annualized Return for Trading Strategy: {annualized_return_model}")
print(f"Annualized Return for S&P 500: {annualized_return_sp500}")

# Calculate the Sortino ratio for the trading strategy and the S&P 500
def calculate_sortino_ratio(data):
    returns = data['Return']
    downside_returns = returns[returns < 0]
    sortino_ratio = returns.mean() / downside_returns.std()
    return sortino_ratio

sortino_ratio_model = calculate_sortino_ratio(model_and_signals)
sortino_ratio_sp500 = calculate_sortino_ratio(sp500_features)

print(f"Sortino Ratio for Trading Strategy: {sortino_ratio_model}")
print(f"Sortino Ratio for S&P 500: {sortino_ratio_sp500}")

# Calculate the Calmar ratio for the trading strategy and the S&P 500
def calculate_calmar_ratio(data):
    cum_return = data['Cumulative_Strategy_Return']
    max_drawdown = calculate_max_drawdown(data)
    calmar_ratio = cum_return[-1] / abs(max_drawdown)
    return calmar_ratio

calmar_ratio_model = calculate_calmar_ratio(model_and_signals)
calmar_ratio_sp500 = calculate_calmar_ratio(sp500_features)

print(f"Calmar Ratio for Trading Strategy: {calmar_ratio_model}")
print(f"Calmar Ratio for S&P 500: {calmar_ratio_sp500}")

# Write all the performance metrics to a CSV file
performance_metrics = {
    'Sharpe Ratio': [sharpe_ratio_model, sharpe_ratio_sp500],
    'Max Drawdown': [max_drawdown_model, max_drawdown_sp500],
    'Annualized Return': [annualized_return_model, annualized_return_sp500],
    'Sortino Ratio': [sortino_ratio_model, sortino_ratio_sp500],
    'Calmar Ratio': [calmar_ratio_model, calmar_ratio_sp500]
}

performance_metrics_df = pd.DataFrame(performance_metrics, index=['Trading Strategy', 'S&P 500'])
performance_metrics_df.to_csv("performance_metrics.csv")
print(performance_metrics_df)

# Plot the cumulative returns of the trading strategy and the S&P 500

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

# Create a bar chart comparing the Calmar ratio of the trading strategy and the S&P 500
performance_metrics_df['Calmar Ratio'].plot(kind='bar', figsize=(12, 6))
plt.title('Calmar Ratio of Trading Strategy vs. S&P 500')
plt.ylabel('Calmar Ratio')
plt.grid()
plt.show()


# Create a bar chart of the performance metrics, excluding the Calmar ratio
performance_metrics_df.drop('Calmar Ratio', axis=1).plot(kind='bar', figsize=(12, 6))
plt.title('Performance Metrics of Trading Strategy vs. S&P 500')
plt.ylabel('Value')
plt.grid()
plt.show()

# Plot the predicted return and actual return
plt.figure(figsize=(12, 6))
plt.plot(model_and_signals['Predicted_Return'], label='Predicted Return')
plt.plot(model_and_signals['Return'], label='Actual Return')
plt.legend()
plt.title('Predicted Return vs. Actual Return')
plt.xlabel('Date')
plt.ylabel('Return')
plt.grid()
plt.show()

# Create candlestick chart for the new data

fig = go.Figure(
    data=[go.Candlestick(x=new_features.index,
        open=new_features['Open'],
        high=new_features['High'],
        low=new_features['Low'],
        close=new_features['Close'])])
# label it
fig.update_layout(title=f'{ticker} Candlestick Chart',
                        xaxis_title='Date',
                        yaxis_title='Price')
fig.show()

# Create candlestick chart for the S&P 500 data
fig = go.Figure(
    data=[go.Candlestick(x=sp500_features.index,
        open=sp500_features['Open'],
        high=sp500_features['High'],
        low=sp500_features['Low'],
        close=sp500_features['Close'])])
# label it
fig.update_layout(title='S&P 500 Candlestick Chart',
                        xaxis_title='Date',
                        yaxis_title='Price')
fig.show()

# Create a scatter plot of the strategy return vs. the volatility
plt.figure(figsize=(12, 6))
plt.scatter(model_and_signals['Strategy_Return'], model_and_signals['Volatility'])
plt.title('Strategy Return vs. Volatility')
plt.xlabel('Strategy Return')
plt.ylabel('Volatility')
plt.grid()
plt.show()

# Create a bar chart that compares the strategy return vs. the S&P 500 return
plt.figure(figsize=(12, 6))
plt.bar(model_and_signals.index, model_and_signals['Strategy_Return'], label='Strategy Return')
plt.bar(sp500_features.index, sp500_features['Return'], label='S&P 500 Return')
plt.legend()
plt.title('Strategy Return vs. S&P 500 Return')
plt.xlabel('Date')
plt.ylabel('Return')
plt.grid()
plt.show()

# Create a line chart that compares the strategy return vs. the S&P 500 return
plt.figure(figsize=(12, 6))
plt.plot(model_and_signals['Strategy_Return'], label='Strategy Return')
plt.plot(sp500_features['Return'], label='S&P 500 Return')
plt.legend()
plt.title('Strategy Return vs. S&P 500 Return')
plt.xlabel('Date')
plt.ylabel('Return')
plt.grid()
plt.show()