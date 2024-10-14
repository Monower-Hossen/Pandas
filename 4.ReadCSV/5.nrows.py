import pandas as pd

df = pd.read_csv('data.csv', nrows=5)  # read only the first 100 rows
print(df)

df = pd.read_csv('data.csv', usecols=['Duration'])
print(df.to_string())

df = pd.read_csv('data.csv', skiprows=2)  # skips the first two rows
print(df.to_string())

df = pd.read_csv('data.csv')
print(df.describe())