'''There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.'''

#Print the last 10 rows of the DataFrame:

import  pandas as pd

df  = pd.read_csv('data.csv')

print(df.tail(10))