#labeling - label can be used to access a specified value:

import pandas as pd
x = [1,5,6]
variable = pd.Series(x)
print(variable[1])


#With create label you can create your own name labels:

import pandas as pd
a = [1,5,6]
variable = pd.Series(a, index=["x","y","z"])
print(variable)


#type
import pandas as pd
a = [1,5,6]
variable = pd.Series(a, index=["x","y","z"] ,dtype = 'float' , name= 'pandas')
print(variable)
