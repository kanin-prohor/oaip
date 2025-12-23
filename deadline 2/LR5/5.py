math = {"Alice", "Bob", "Charlie", "David"}
physics = {"Bob", "David", "Eve", "Frank"}
cs = {"Alice", "Charlie", "Eve", "Grace"}

all_three = math & physics & cs
print(f"Все три курса: {all_three if all_three else 'нет'}")

only_one = (math ^ physics ^ cs) - (math & physics) - (math & cs) - (physics & cs)
print(f"Только один курс: {only_one if only_one else 'нет'}")

math_not_physics = math - physics
print(f"Математика, но не физика: {math_not_physics}")

all_students = math | physics | cs
print(f"Всего студентов: {len(all_students)}")