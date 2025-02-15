import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2010-01-01"
    end_date = "2020-01-01"
    data = download_stock_data(ticker, start_date, end_date)
    data.to_csv(f"{ticker}_data.csv")
