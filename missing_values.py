import pandas as pd

# Load dataset
df = pd.read_csv("employee_data.csv")

# -----------------------------
# BEFORE CLEANING
# -----------------------------

print("Original Dataset:\n")
print(df)

# Check missing values
print("\nMissing Values Count:\n")
print(df.isnull().sum())

# -----------------------------
# dropna() Example
# -----------------------------

print("\nDataset after dropna():\n")

# Remove rows with missing values
drop_data = df.dropna()

print(drop_data)

# -----------------------------
# fillna() Example
# -----------------------------

print("\nDataset after fillna():\n")

# Fill missing values
fill_data = df.fillna({
    "Salary": 0,
    "City": "Unknown"
})

print(fill_data)