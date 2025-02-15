import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error

def evaluate_model(model, data):
    X = data[['Volatility', 'Momentum']]
    y = data['Return']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    file_path = "AAPL_data_features.csv"
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = xgb.XGBRegressor()
    model.load_model("xgboost_model.json")
    evaluate_model(model, data)
