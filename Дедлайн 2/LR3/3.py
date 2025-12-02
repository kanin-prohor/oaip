phone_book = {
    "Анна": "+7-911-123-45-67",
    "Иван": "+7-912-987-65-43",
    "Мария": "+7-913-555-55-55"
}
while True:
    print("\nМеню:")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("\nКонтакты:")
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста")
    elif choice == "2":
        name = input("Имя: ")
        if name in phone_book:
            print("Контакт уже существует!")
        else:
            phone = input("Телефон: ")
            phone_book[name] = phone
            print("Контакт добавлен!")
    elif choice == "3":
        name = input("Имя контакта для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт удален!")
        else:
            print("Контакт не найден!")
    elif choice == "4":
        print("До свидания!")
        break
    else:
        print("Неверный выбор!")