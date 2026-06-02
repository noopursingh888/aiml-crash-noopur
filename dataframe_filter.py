import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

# Select specific columns
selected_columns = df[["Name", "Course", "Marks"]]

print("Selected Columns:")
print(selected_columns)

print("\nFiltered Data:")

# Filter rows
# Condition 1: Course should be AIML
# Condition 2: Marks should be greater than 80

filtered_data = df[
    (df["Course"] == "AIML") &
    (df["Marks"] > 80)
]

# Print filtered result
print(filtered_data)