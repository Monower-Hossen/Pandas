'''replacing the empty value : we will use the fillna() method
which will allow us to replace the empty cell with a value.
'''
#Replace NULL values with the number 130:

import pandas as pd
a = pd.read_csv('data.csv')
a.fillna(130 , inplace=True)
print(a.to_string())

'''to replace only the empty value for one column , 
you need to specify the column name.
'''
#Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd
a = pd.read_csv('data.csv')
a["Calories"].fillna (130, inplace = True )
print(a.to_string())
