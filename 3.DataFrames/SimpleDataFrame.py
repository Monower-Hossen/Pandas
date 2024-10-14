#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,or a table with rows and columns.

#Create a simple Pandas DataFrame:

import pandas as pd

# Dictionary containing data
INFO = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(INFO)

# Print the DataFrame
print(df)
