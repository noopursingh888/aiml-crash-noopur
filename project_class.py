# Class representing a learner

class Learner:

    # Constructor
    def __init__(self, name: str, course: str, skill: str):
        self.name = name
        self.course = course
        self.skill = skill

    # Method
    def learner_profile(self) -> str:
        return (
            f"Learner Name : {self.name}\n"
            f"Course        : {self.course}\n"
            f"Main Skill    : {self.skill}"
        )


# Object Creation
student1 = Learner(
    "Noopur Singh",
    "Artificial Intelligence & Machine Learning",
    "Python"
)

# Method Call
print(student1.learner_profile())