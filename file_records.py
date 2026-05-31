# This program reads and writes CSV files
# and calculates student averages and grades


import csv


# Create students.csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["name", "math", "science", "english"])

    writer.writerow(["Noopur", 90, 85, 95])
    writer.writerow(["khushbu", 70, 65, 75])
    writer.writerow(["kalpana", 50, 55, 60])


# Function to calculate grade

def calculate_grade(avg):

    if avg >= 90:
        return "A"

    elif avg >= 75:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 35:
        return "D"

    else:
        return "F"


# Read students.csv and create results.csv

with open("students.csv", "r") as input_file, \
     open("results.csv", "w", newline="") as output_file:

    reader = csv.DictReader(input_file)

    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:

        math = int(row["math"])
        science = int(row["science"])
        english = int(row["english"])

        average = (math + science + english) / 3

        grade = calculate_grade(average)

        writer.writerow({
            "name": row["name"],
            "average": round(average, 2),
            "grade": grade
        })


print("students.csv created")
print("results.csv created")