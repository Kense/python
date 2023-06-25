import yfinance as yf
import pandas as pd

# Specify the stock symbol for Taiwan's stock exchange (TWSE)
stock_symbol = "2330.TW"  # Example: Taiwan Semiconductor Manufacturing Company (TSMC)

# Fetch the stock data
stock_data = yf.download(stock_symbol, start="2023-01-1", end="2023-06-30")

# Convert the fetched data to a DataFrame
df = pd.DataFrame(stock_data)

#fetch the last 3 data
new_df= df.tail(3)

# Save the DataFrame to a CSV file
df.to_csv("stock_data.csv", index=False)




