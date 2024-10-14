import pandas as pd

df = pd.read_csv('data.csv', header=None)

print(df)


df = pd.read_csv('data.csv', skiprows=2)  # skips the first two rows
print(df)
