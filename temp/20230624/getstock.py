import yfinance as yf
import pandas as pd


# Specify the stock symbol for Taiwan's stock exchange (TWSE)
stock_symbol = "2330.TW"  # Example: Taiwan Semiconductor Manufacturing Company (TSMC)

# Fetch the stock data
stock_data = yf.download(stock_symbol, start="2023-06-1", end="2023-06-30")

# Convert the fetched data to a DataFrame
df = pd.DataFrame(stock_data)

# Extract the "Close" column
close_price = df["Close"].values[0]
# Print the fetched data
print(close_price)
