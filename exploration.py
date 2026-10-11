import pandas as pd

data = pd.read_csv("C:\\Users\\vv519\\Downloads\\groceries (2).csv")

print("First 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(data.columns)

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

print("\nStatistics:")
print(data.describe())