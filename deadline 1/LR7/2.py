print("=== РЕГИСТРАЦИЯ ===")
password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")
if password != confirm_password:
    print("Ошибка: пароли не совпадают!")
else:
    print("Пароль успешно установлен!")
    print("\n=== АВТОРИЗАЦИЯ ===")
    login_password = input("Введите пароль для входа: ")
    if login_password == password:
        print("Access")
    else:
        print("Denied")