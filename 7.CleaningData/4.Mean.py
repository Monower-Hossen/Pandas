#calculate the MEAN and replace the empty values with it.

import pandas as pd
a = pd.read_csv('data.csv')
x = a['Calories'].mean()
a['Calories'].fillna(x , inplace = True)
print(a.to_string())