import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model(data):
    X = data[['Volatility', 'Momentum']]
    y = data['Return']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model

if __name__ == "__main__":
    file_path = "AAPL_data_features.csv"
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    model = train_model(data)
    model.save_model("xgboost_model.json")
