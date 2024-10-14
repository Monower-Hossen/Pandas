import pandas as pd

# Create a DataFrame
data = {
    'A': [10, 20, 30, 40],
    'B': [5, 6, 7, 8]
}

# Create DataFrame with custom index
var = pd.DataFrame(data)

# Print the initial DataFrame
print(var)

# Add column 'C' by summing 'A' and 'B'
var['C'] = var['A'] + var['B']
print("\n",var)

# Modify column 'C' by subtracting 'B' from 'A'
var['C'] = var['A'] - var['B']
print("\n",var)

# Modify column 'C' by multiplying 'A' and 'B'
var['C'] = var['A'] * var['B']
print("\n",var)

# Modify column 'C' by dividing 'A' by 'B'
var['C'] = var['A'] / var['B']
print("\n",var)

# Create a new boolean column 'python' based on condition
var['python'] = var['A'] <= 20
print("\n",var)