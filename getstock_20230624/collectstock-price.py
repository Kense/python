import yfinance as yf
import pandas as pd

# Specify the stock symbols for Taiwan's stock exchange (TWSE)
stock_symbols = ["2330.TW", "3231.TW"]

# Specify the date range for which you want to fetch the stock data
start_date = "2023-01-01"
end_date = "2023-06-23"

# Create an empty DataFrame to store the closing prices
df = pd.DataFrame()
i=0
# Loop through each stock symbol and extract the closing prices
for stock_symbol in stock_symbols:
    # Fetch the stock data for the date range
    stock_data = yf.download(stock_symbols[i], start=start_date, end=end_date)

    # Extract the closing prices for the current stock symbol
    close_prices = stock_data["Close"]

    # Create a temporary DataFrame with the date and close price for the current stock symbol
    temp_df = pd.DataFrame({"Date": close_prices.index, stock_symbols[i]: close_prices.values})
    # Merge the temporary DataFrame with the main DataFrame
    if (i!=0):
        df = pd.merge(df, temp_df, on="Date")
    else:
        df=temp_df    
    # Increment the counter variable i
    i += 1

# Save the DataFrame to a CSV file
df.to_csv("merge-closing_prices.csv", index=False)
print(df)   
