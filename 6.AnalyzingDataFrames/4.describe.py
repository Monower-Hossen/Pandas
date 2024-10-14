import pandas as pd

df = pd.read_csv('data.csv')

print(df.describe())

print(df[10:14])