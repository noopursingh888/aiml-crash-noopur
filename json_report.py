import json

# Load JSON file
with open("student.json", "r") as file:
    data = json.load(file)

# List comprehension
skills = [skill.upper() for skill in data["skills"]]

# Print report using f-strings
print(f"Student Name : {data['name']}")
print(f"Role          : {data['role']}")
print(f"Skills        : {', '.join(skills)}")