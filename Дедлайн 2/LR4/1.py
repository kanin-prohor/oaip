grades = []
grades.extend([4, 5, 3, 4, 2])
print(f"Текущие оценки: {grades}")
grades = grades[1:-1] if len(grades) > 2 else []
print(f"Средний балл: {sum(grades)/len(grades):.2f}" if grades else "Нет оценок")
print(f"Итоговые оценки: {grades}")