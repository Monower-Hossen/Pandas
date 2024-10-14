#Load the JSON file into a DataFrame:

import pandas as pd
a = pd.read_json('csvjson.json')
print(a.to_string())






