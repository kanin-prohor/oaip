students = [
    ("Анна", 19, 4.5),
    ("Иван", 21, 3.8),
    ("Мария", 20, 4.9),
    ("Петр", 22, 4.2),
    ("Ольга", 18, 4.7)
]

print("Старше 20 лет:")
for name, age, score in students:
    if age > 20:
        print(f"{name}, {age} лет, балл: {score}")

best_student = max(students, key=lambda x: x[2])
print(f"Лучший студент: {best_student[0]} с баллом {best_student[2]}")

print("Сортировка по имени:")
for name, age, score in sorted(students):
    print(f"{name}: {age} лет, {score} баллов")