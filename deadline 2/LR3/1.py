fruits = {
    "яблоки": 5,
    "бананы": 3,
    "апельсины": 10,
    "арбузы": 33
}
print("Начальное количество фруктов:")
for fruit, count in fruits.items():
    if count == 1:
        print(f"За прилавком есть {count} {fruit[:-1]}")
    else:
        print(f"За прилавком есть {count} {fruit}")
fruits["яблоки"] -= 2
print(f"\nПродали 2 яблока.")
fruits["арбузы"] = 0
print("Ашот Похититель Арбузов украл все арбузы!")
print("\nИтоговое количество фруктов:")
for fruit, count in fruits.items():
    if count == 1:
        print(f"За прилавком осталось {count} {fruit[:-1]}")
    else:
        print(f"За прилавком осталось {count} {fruit}")