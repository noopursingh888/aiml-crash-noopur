name = "Noopur"
age = 19
city = "lucknow"
favorite_subject = "oops"
target_role = "Data Engineer"
student = {
    "name": name,
    "age": age,
    "city": city,
    "favorite_subject": favorite_subject,
    "target_role": target_role
}
print(f"My name is {student['name'].title()}.")

print(f"I live in {student['city']}.")

print(f"My favorite subject is {student['favorite_subject'].upper()}.")

print(f"My target role is {student['target_role']}.")