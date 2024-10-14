# read csv files : (comma separated files) it is a simple way to store the big and bigest data sets.csv files contains plains text.

#loading the csv into a dataframe with to_string:

import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())


#loading the csv into a dataframe without to_string:

import pandas as pd

df = pd.read_csv ('data.csv')
print(df)

