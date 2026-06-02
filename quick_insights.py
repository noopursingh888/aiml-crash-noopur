import pandas as pd

# Load dataset
df = pd.read_csv("employee_data.csv")

# --------------------------------
# describe() on numeric column
# --------------------------------

print("Salary Statistics:\n")

salary_stats = df["Salary"].describe()

print(salary_stats)

# Observation
print("\nObservation:")
print("The average salary is around 52,400.")

# --------------------------------
# value_counts() on categorical column
# --------------------------------

print("\nDepartment Counts:\n")

department_counts = df["Department"].value_counts()

print(department_counts)

# Observation
print("\nObservation:")
print("Most employees belong to the AIML department.")