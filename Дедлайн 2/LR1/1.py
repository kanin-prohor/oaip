num = int(input("Введите положительное целое число: "))
if num <= 0:
    print("Ошибка: введите положительное число")
else:
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    print(f"Сумма цифр: {total}")