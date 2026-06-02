# Student Profile Card using F-Strings and Type Hints

# Variables
name: str = "Noopur Singh"
age: int = 19
course: str = "Computer Science"
college: str = "ACEIT"

# Dictionary
student_profile: dict = {
    "Name": name,
    "Age": age,
    "Course": course,
    "College": college
}

# Function with Type Hints
def create_profile(profile: dict) -> str:
    return (
        f"Student Name : {profile['Name']}\n"
        f"Age           : {profile['Age']}\n"
        f"Course        : {profile['Course']}\n"
        f"College       : {profile['College']}"
    )

# Output
print(create_profile(student_profile))