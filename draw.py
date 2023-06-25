import matplotlib.pyplot as plt

# Table A data
dates = ["2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-09", "2023-01-10", "2023-01-11"]
values = [453.0, 449.5, 458.5, 458.5, 481.0, 486.0, 484.5]

# Plot the diagram
plt.plot(dates, values, marker='o')

# Set labels and title
plt.xlabel('Date')
plt.ylabel('2330.TW')
plt.title('2330.TW Value Over Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the diagram
plt.show()
