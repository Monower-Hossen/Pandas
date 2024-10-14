
# here we will return a new data frame with no empty cell.

import pandas as pd

a = pd.read_csv('data.csv')
aNew = a.dropna()

print(aNew.to_string())

'''if at any case you want to change the original dataframe ,
then use the inplace = True argument.it will remove the rows
containing the NULL (NaN) value.'''

import pandas as pd

a = pd.read_csv('data.csv')
a.dropna(inplace = True)

print(a.to_string())
