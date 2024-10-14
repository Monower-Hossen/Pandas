import pandas as pd

# Data dictionary
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Load data into a DataFrame object
df = pd.DataFrame(data)

# Print the row at index 2
print("Row at index 2:")
print(df.loc[2])

# Print the row at index 1
print("\nRow at index 1:")
print(df.loc[1])

# Use a list of indexes to print rows at index 0 and 1
print("\nRows at indexes 0 and 1:")
print(df.loc[[0, 1]])
