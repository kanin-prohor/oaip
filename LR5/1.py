num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
num1 = float(num1)
num2 = float(num2)
print("\nРезультаты вычислений:")
print(f"Сложение: {num1} + {num2} = {num1 + num2}")
print(f"Вычитание: {num1} - {num2} = {num1 - num2}")
print(f"Умножение: {num1} × {num2} = {num1 * num2}")
if num2 != 0:
    print("Деление: {num1} ÷ {num2} = {num1 / num2}")
else:
    print("Деление: невозможно (деление на ноль)")