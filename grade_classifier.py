students = [
    {"name": "Noopur", "score": 95},
    {"name": "Rahul", "score": 82},
    {"name": "Priya", "score": 74},
    {"name": "Aman", "score": 61},
    {"name": "Riya", "score": 40}
]


def classify(score):

    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 35:
        return "D"

    else:
        return "F"


sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)


for student in sorted_students:

    grade = classify(student["score"])

    print(f"{student['name']} scored {student['score']} and got grade {grade}")