
#You can also remove the rows for wrong data in large dataset:

import pandas as pd

df = pd.read_csv('data.csv')

for i in df.index:
    if df.loc[i,"Duration"] > 120 :
        df.drop(i , inplace= True)

print(df.to_string())