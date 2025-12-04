# WGU C964 Capstone: Ensemble Model Investment Platform

## Project Overview

This project develops an Ensemble Model (EM) investment platform using machine learning to generate daily buy/sell signals for stock trading. The platform aims to democratize data-driven investment decisions for working-class Americans by providing accessible, automated trading recommendations.

**Institution:** Western Governors University  
**Course:** C964 - Computer Science Capstone  
**Author:** Timothy Javins  
**Fictional Organization:** Global Investment Solutions

## Problem Statement

With rising costs of living and increasing wealth disparity, 61% of Americans live paycheck-to-paycheck (LendingClub & PYMNTS.com, 2022). Despite platforms like Robinhood and Acorns lowering entry barriers, people lack the time and expertise to make informed investment decisions. This project addresses this gap by providing automated, data-driven trading signals.

## Solution

The Ensemble Model uses Extreme Gradient Boosting (XGBoost) to predict stock price movements and generate buy/sell signals. By training on historical stock data, the model aims to outperform traditional buy-and-hold strategies while remaining accessible to novice investors.

## Features

- **Machine Learning Model**: XGBoost regression model for predicting daily returns
- **Feature Engineering**: Volatility and momentum indicators derived from price data
- **Backtesting Framework**: Historical performance evaluation against S&P 500
- **Performance Metrics**: Sharpe Ratio, Sortino Ratio, Calmar Ratio, Max Drawdown, Annualized Return
- **Visualizations**: 
  - Cumulative return comparisons
  - Candlestick charts
  - Performance metric bar charts
  - Strategy return analysis

## Project Structure

```
├── all-code.py                 # Complete pipeline implementation
├── data_collection.py          # Yahoo Finance data download
├── data_preprocessing.py       # Data cleaning and preparation
├── feature_engineering.py      # Technical indicator calculation
├── model_training.py           # XGBoost model training
├── model_evaluation.py         # Model performance evaluation
├── trading_strategy.py         # Signal generation and strategy implementation
├── backtesting.py              # Historical performance testing
├── EnsembleModel.ipynb         # Interactive notebook version
├── 1yoModel.ipynb              # 1-year training horizon model
├── 4yoModel.ipynb              # 4-year training horizon model
└── forms/                      # Project documentation
    ├── Javins C964 Capstone - letter of transmittal.md
    ├── Javins C964 Capstone - project proposal.md
    └── Javins C964 Capstone - post-implementation report.md
```

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Required Libraries

```bash
pip install pandas numpy yfinance xgboost scikit-learn matplotlib plotly
```

## Usage

### Complete Pipeline

Run the entire pipeline from data collection to visualization:

```bash
python all-code.py
```

### Individual Modules

#### 1. Data Collection

````python
from data_collection import download_stock_data

ticker = "AAPL"
start_date = "2010-01-01"
end_date = "2024-01-01"
data = download_stock_data(ticker, start_date, end_date)
data.to_csv(f"{ticker}_data.csv")
````

#### 2. Data Preprocessing

````python
from data_preprocessing import preprocess_data

data = preprocess_data("AAPL_data.csv")
data.to_csv("AAPL_data_preprocessed.csv")
````

#### 3. Feature Engineering

````python
from feature_engineering import create_features

data = create_features(data)
data.to_csv("AAPL_data_features.csv")
````

#### 4. Model Training

````python
from model_training import train_model
import xgboost as xgb

model = train_model(data)
model.save_model("xgboost_model.json")
````

#### 5. Trading Strategy Implementation

````python
from trading_strategy import implement_strategy

model = xgb.XGBRegressor()
model.load_model("xgboost_model.json")
strategy_data = implement_strategy(model, data)
strategy_data.to_csv("AAPL_strategy.csv")
````

#### 6. Backtesting

````python
from backtesting import backtest_strategy

backtest_results = backtest_strategy(strategy_data)
backtest_results.to_csv("AAPL_backtest.csv")
````

### Interactive Notebooks

Launch Jupyter notebooks for interactive exploration:

```bash
jupyter notebook EnsembleModel.ipynb
```

## Data Source

- **Provider**: Yahoo Finance via [`yfinance`](https://github.com/ranaroussi/yfinance)
- **Data Type**: Daily OHLCV (Open, High, Low, Close, Volume)
- **Privacy**: Publicly available, no PII concerns

## Model Details

### Features

- **Volatility**: 21-day rolling standard deviation of returns
- **Momentum**: 21-day rolling average of closing prices

### Target Variable

- **Tomorrow's Return**: Next day's percentage change in closing price

### Algorithm

- **XGBoost Regressor**
  - Objective: `reg:squarederror`
  - Estimators: 1000

### Trading Signals

- **Buy (1)**: Predicted return > 0
- **Sell (-1)**: Predicted return ≤ 0

## Performance Metrics

The model is evaluated using industry-standard metrics:

- **Sharpe Ratio**: Risk-adjusted return
- **Sortino Ratio**: Downside risk-adjusted return
- **Calmar Ratio**: Return relative to maximum drawdown
- **Maximum Drawdown**: Largest peak-to-trough decline
- **Annualized Return**: Yearly return rate

Results are compared against a buy-and-hold S&P 500 strategy.

## Key Findings

The project demonstrates that:
1. Model training frequency impacts performance (see `1yoModel.ipynb` vs `4yoModel.ipynb`)
2. Regular retraining (monthly/weekly) is necessary for adapting to market changes
3. Simple features (volatility, momentum) can generate meaningful trading signals

## Project Methodology

The project follows an **Agile** approach with:
- Iterative development sprints
- Continuous integration and testing
- Regular stakeholder feedback
- Incremental feature releases

## Documentation

Comprehensive project documentation is available in the forms directory:

- **[Letter of Transmittal](forms/Javins%20C964%20Capstone%20-%20letter%20of%20transmittal.md)**: Executive summary and approval request
- **[Project Proposal](forms/Javins%20C964%20Capstone%20-%20project%20proposal.md)**: Problem statement, solution, methodology, and timeline
- **[Post-Implementation Report](forms/Javins%20C964%20Capstone%20-%20post-implementation%20report.md)**: Stakeholder impact and governance considerations

## Future Enhancements

Potential improvements identified:

1. **Community Features**: Social investing and peer sharing
2. **Gamification**: Engagement elements to make investing accessible
3. **Automated Retraining**: Scheduled model updates
4. **Transaction Costs**: Incorporation of fees and slippage
5. **Risk Management**: Position sizing and stop-loss rules
6. **Multi-Asset Support**: Expansion beyond single stocks

## Limitations

- **Look-Ahead Bias**: Careful signal shifting implemented to prevent data leakage
- **Transaction Costs**: Not currently modeled
- **Execution Assumptions**: Assumes trading at closing prices
- **Single Asset**: Currently limited to one stock at a time
- **Daily Granularity**: No intraday trading support--avoiding Pattern Dat Trader (PDT) complications

## License

This project is submitted as academic work for WGU C964 Capstone. All rights reserved.

## References

- LendingClub & PYMNTS.com (2022). *Reality Check: The Paycheck-To-Paycheck Report*
- U.S. Census Bureau (2024). *Income and Poverty in the United States*
- Yahoo Finance API via `yfinance` library

## Fictional Contact

**Timothy Javins**  
Project Manager  
Global Investment Solutions  
timothy.javins@gis.ai

---

**Note**: This is a proof-of-concept academic project. Not intended for real trading without further development, testing, and compliance review.
