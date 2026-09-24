from dataclasses import dataclass


class TraditionalStudent:
    def __init__(self, student_id: int, name: str, age: int, course: str, cgpa: float):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.cgpa = cgpa

    def display(self) -> None:
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"CGPA: {self.cgpa}")


@dataclass
class Student:
    student_id: int
    name: str
    age: int
    course: str
    cgpa: float

    def display(self) -> None:
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"CGPA: {self.cgpa}")


traditional_student = TraditionalStudent(
    101,
    "lokesh",
    22,
    "M.Tech CSE",
    9.34
)

dataclass_student = Student(
    102,
    "Rahul",
    23,
    "M.Tech CSE",
    8.95
)

print("TRADITIONAL CLASS")
traditional_student.display()

print("\nDATACLASS")
dataclass_student.display()

print("\nCOMPARISON")
print("Traditional class requires an explicit __init__() method.")
print("Dataclass automatically generates __init__(), __repr__(), and __eq__().")