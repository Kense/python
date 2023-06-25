import yfinance as yf
import pandas as pd

# Specify the stock symbols for Taiwan's stock exchange (TWSE)
stock_symbols = ["2330.TW", "3231.TW", "4979.TW"]

# Specify the date range for which you want to fetch the stock data
start_date = "2023-01-01"
end_date = "2023-06-23"


# Fetch the stock data for the date range
stock_data = yf.download(stock_symbols[0], start=start_date, end=end_date)

# Create an empty DataFrame to store the closing prices
df = pd.DataFrame()


# Extract the closing prices for the current stock symbol
close_prices = stock_data["Close"]

 
# Create a temporary DataFrame with the date and close price for the current stock symbol
temp_df = pd.DataFrame({"Date": close_prices.index, stock_symbols[0]: close_prices.values})
 
print(temp_df)   
