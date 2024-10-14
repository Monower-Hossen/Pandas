#Named Indexes

import pandas as pd

# Data dictionary
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create DataFrame with custom index
df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# Print the DataFrame
print(df)

# Print the type of df
print(type(df))


#refer to the named index:
print(df.loc["day2"])
