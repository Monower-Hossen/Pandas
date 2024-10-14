#calculate the MODE and replace the empty cell with it.

import pandas as pd

a = pd.read_csv('data.csv')

x = a["Calories"].mode()[0]
a["Calories"].fillna(x, inplace = True)

print(a.to_string())
