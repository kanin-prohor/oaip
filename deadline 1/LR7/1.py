direction = input("Введите направление (left, right, straight, back): ").strip().lower()
if direction == "straight":
    print("Иду прямо")
elif direction == "left":
    print("Иду влево")
elif direction == "right":
    print("Иду вправо")
elif direction == "back":
    print("Иду назад")
else:
    print("Неправильное направление")