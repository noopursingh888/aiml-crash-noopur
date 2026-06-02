import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Complete Dataset:")
print(df)

# -----------------------------------
# Using .loc (label-based selection)
# -----------------------------------

print("\nUsing .loc :")

# Select row label 2 and columns Name & Marks
loc_data = df.loc[2, ["Name", "Marks"]]

print(loc_data)

# -----------------------------------
# Using .iloc (position-based selection)
# -----------------------------------

print("\nUsing .iloc :")

# Select row position 2 and column positions 0 & 2
iloc_data = df.iloc[2, [0, 2]]

print(iloc_data)

# -----------------------------------
# Difference Explanation
# -----------------------------------

print("\nDifference:")
print(".loc selects data using row/column labels.")
print(".iloc selects data using row/column positions.")