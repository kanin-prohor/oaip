tasks = []

while True:
    print("\n1. Показать задачи\n2. Добавить\n3. Удалить\n4. Выйти")
    choice = input("Выбор: ")
    
    if choice == "1":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
    elif choice == "2":
        task = input("Задача: ")
        if task:
            tasks.append(task)
    
    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            num = int(input("Номер для удаления: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        except:
            print("Ошибка")

    elif choice == "4":
        break