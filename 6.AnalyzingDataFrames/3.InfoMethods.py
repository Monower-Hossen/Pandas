#Print information about the data:

import  pandas as pd

df  = pd.read_csv('data.csv')

print(df.info())