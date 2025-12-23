year = int(input("Введите год: "))
if year % 4 != 0:
    print(f"{year} год - невисокосный")
elif year % 100 != 0:
    print(f"{year} год - високосный")
elif year % 400 != 0:
    print(f"{year} год - невисокосный")
else:
    print(f"{year} год - високосный")