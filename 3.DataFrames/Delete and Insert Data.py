import pandas as pd

# Creating a DataFrame with three columns
var = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [5, 6, 7, 8], 'C': [50, 21, 25, 28]})

print("Initial DataFrame:")
print(var)

# Insert column 'python' at index 1 using the values from column 'A'
var.insert(1, 'python', var["A"])
print("\nDataFrame after inserting 'python' at index 1:")
print(var)

# Insert a new column 'python_1' at index 1 using a list of values
# Ensure that the number of elements in the list matches the number of rows in the DataFrame
var.insert(1, 'python_1', [11, 12, 13, 14])
print("\nDataFrame after inserting 'python_1' at index 1:")
print(var)

# Add a new column 'python_12' using only the first three values of column 'A'
# Use the `.iloc` attribute to handle this appropriately and fill missing values
var["python_12"] = var["A"].iloc[:3].tolist() + [None]
print("\nDataFrame after adding 'python_12' with the first three values of 'A':")
print(var)

# Delete column 'B' and store it in var1 using the .pop() method
var1 = var.pop('B')
print("\nValues of the deleted 'B' column stored in var1:")
print(var1)
