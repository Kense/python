import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file using pandas
data = pd.read_csv('price_round.csv')

# Convert the 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Calculate the average '2330.TW' values for each week
weekly_data = data.resample('W', on='Date').mean()

# Extract the Date and 2330.TW columns
dates = weekly_data.index
values = weekly_data['2330.TW']

# Plot the diagram
plt.plot(dates, values, marker='o')

# Set labels and title
plt.xlabel('Date')
plt.ylabel('2330.TW Average')
plt.title('Weekly Average 2330.TW Value')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the diagram
plt.show()
