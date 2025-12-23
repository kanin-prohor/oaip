import random
secret_number = random.randint(1, 100)
attempts = 0
print("Я загадал число от 1 до 100. Попробуй угадать!")
while True:
    try:
        guess = int(input("Введите вашу догадку: "))
        attempts += 1
        if guess < secret_number:
            print("Больше!")
        elif guess > secret_number:
            print("Меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break
    except ValueError:
        print("Пожалуйста, введите целое число.")