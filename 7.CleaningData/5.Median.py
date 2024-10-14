#calculate the MEDIAN and replace any empty values in it :

import pandas as pd

df = pd.read_csv('data.csv')
value = df['Calories'].median()
df['Calories'].fillna(value, inplace = True)

print(df.to_string())

