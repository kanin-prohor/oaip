text = input("Введите произвольный текст: ")
try:
    step = int(input("Введите шаг: "))
    if step <= 0:
        print("Ошибка: шаг должен быть положительным числом")
    else:
        result = text[::step]
        print(f"\nТекст с шагом {step}:")
        print(result)
except ValueError:
    print("Ошибка: пожалуйста, введите целое число для шага")