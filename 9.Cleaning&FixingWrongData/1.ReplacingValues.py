#Wrong Data:  Its only  a wrong data

#Loading and reading the original dataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())

#Here we will set "Duration " = 60 in row 4 :

import pandas as pd

df = pd.read_csv('data.csv')
df.loc[4,"Duration"] = 60

print(df.to_string())


'''for larger data set: Now here we will loop through all the values 
in "Duration" column,if the value is higher than 120 and set it to 120.'''

import pandas as pd

df = pd.read_csv('data.csv')

for i in df.index:
    if df.loc[i,"Duration"] > 120 :
        df.loc[i, "Duration"] = 120

print(df.to_string())
