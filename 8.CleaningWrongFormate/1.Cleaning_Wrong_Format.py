#data in wrong format: to fix this problems, there are 2 ways: remove the rows or convert all the cells in the same format.

# import pandas as pd
#
# df = pd.read_csv('data.csv')
# print(df.to_string())

#Now let's try to convert all the cells in the date column into date.via to datetime()

import pandas as pd

df = pd.read_csv('data.csv')
df["Date"] = pd.to_datetime(df["Date"])
print(df.to_string())
