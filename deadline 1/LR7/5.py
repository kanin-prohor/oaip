data = input("Введите выражение: ").split()
if len(data) != 3:
    print("Ошибка формата")
else:
    try:
        a, op, b = float(data[0]), data[1], float(data[2])
        if op == '+': result = a + b
        elif op == '-': result = a - b
        elif op == '*': result = a * b
        elif op == '/': result = a / b if b != 0 else "Ошибка: деление на 0"
        elif op == '%': result = a % b if b != 0 else "Ошибка: деление на 0"
        elif op == '//': result = a // b if b != 0 else "Ошибка: деление на 0"
        elif op == '**': result = a ** b
        elif op == '%%': result = (b / 100) * a
        elif op == '/**': result = a ** (1/b) if a >= 0 else "Ошибка: корень из отрицательного"
        else: result = "Неизвестная операция"
        print(f"Результат: {result}")
    except: print("Ошибка ввода")