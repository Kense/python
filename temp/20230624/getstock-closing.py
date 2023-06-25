import yfinance as yf
import pandas as pd

# Specify the stock symbol for Taiwan's stock exchange (TWSE)
stock_symbol = "2330.TW"  # Example: Taiwan Semiconductor Manufacturing Company (TSMC)

# Specify the date range for which you want to fetch the stock data
start_date = "2023-01-01"
end_date = "2023-06-23"

# Fetch the stock data for the date range
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Extract the "Close" column
close_prices = stock_data["Close"]

# Create a DataFrame with the date and close price
df = pd.DataFrame({"Date": close_prices.index, stock_symbol: close_prices.values})

# Save the DataFrame to a CSV file
df.to_csv("closing_prices.csv", index=False)
