text = input("Введите произвольный текст: ")
range_input = input("Введите диапазон символов (число1 число2): ")
range_parts = range_input.split()
if len(range_parts) != 2:
    print("Ошибка: пожалуйста, введите ровно два числа через пробел")
else:
    try:
        start = int(range_parts[0])
        end = int(range_parts[1])
        if start < 0 or end < 0:
            print("Ошибка: числа должны быть неотрицательными")
        elif start > end:
            print("Ошибка: первое число должно быть меньше или равно второму")
        elif start >= len(text) or end >= len(text):
            print(f"Ошибка: диапазон выходит за пределы текста (длина текста: {len(text)})")
        else:
            substring = text[start:end+1]
            print(f"\nПодстрока с {start} по {end} символ:")
            print(substring)
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа")