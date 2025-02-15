import pandas as pd
import xgboost as xgb

def implement_strategy(model, data):
    data['Predicted_Return'] = model.predict(data[['Volatility', 'Momentum']])
    data['Signal'] = data['Predicted_Return'].apply(lambda x: 1 if x > 0 else -1)
    data['Strategy_Return'] = data['Signal'] * data['Return']
    return data

if __name__ == "__main__":
    file_path = "AAPL_data_features.csv"
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = xgb.XGBRegressor()
    model.load_model("xgboost_model.json")
    data = implement_strategy(model, data)
    data.to_csv("AAPL_strategy.csv")
