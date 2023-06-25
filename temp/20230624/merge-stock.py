import pandas as pd

# Table A
data_a = {
    "Date": ["2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-09"],
    "2330.TW": [453.0, 449.5, 458.5, 458.5, 481.0]
}
table_a = pd.DataFrame(data_a)

# Table B
data_b = {
    "Date": ["2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-09"],
    "3231.TW": [29.200001, 29.400000, 29.500000, 29.299999, 30.000000]
}
table_b = pd.DataFrame(data_b)

# Merge Table A and Table B on the 'Date' column
merged_table = pd.merge(table_a, table_b, on="Date")

# Print the merged table
print(merged_table)
