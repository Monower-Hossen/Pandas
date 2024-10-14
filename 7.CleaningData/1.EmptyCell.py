
'''cleaning data :it means fixing the bad data in your data set.
Bad data could be : empty cell ,data in a wrong format ,
duplicate data and wrong data'''

#empty cell : it will give you wrong result always , we will have to remove the rows always that contain the bad data.

#loading and reading the original dataframe:

import pandas as pd

a = pd.read_csv('data.csv')

print(a.to_string())

