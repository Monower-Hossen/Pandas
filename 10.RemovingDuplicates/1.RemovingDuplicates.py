#Removing the duplicate values: via you need to discover the duplicate values via duplicate() method.

#Loading and reading the original dataFrame

import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())


#return true for  every rows that is duplicate otherwise return false:

import pandas as pd

df = pd.read_csv('data.csv')
print(df.duplicated())

# removing the duplicate from the data set. via drop_duplicates()

import pandas as pd

df = pd.read_csv('data.csv')
df.drop_duplicates( inplace= True )
print(df.to_string())