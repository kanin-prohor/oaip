from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    average_grade: float

students = [
    Student("Анна", 20, 4.5),
    Student("Иван", 21, 3.8),
    Student("Мария", 19, 4.9),
    Student("Петр", 22, 3.2),
    Student("Ольга", 20, 4.7)
]

students_sorted = sorted(students, key=lambda s: s.average_grade, reverse=True)

for student in students_sorted:
    print(f"{student.name}, {student.age} лет, средний балл: {student.average_grade}")