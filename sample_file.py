# Define a Student class with name, age, and grade atrributes.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


# Method to calculate the grade based on marks.
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

# Create a student object and calculate the grade based on marks.
student1 = Student("Alice", 20, calculate_grade(85))

print(student1.get_grade())  # Output: B


    