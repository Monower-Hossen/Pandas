#You can also use a key/value object, like a dictionary, when creating a Series.
#Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
Info = pd.Series(calories)
print(Info)

#Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
result = pd.Series(calories, index= ["day2"])
print(result)