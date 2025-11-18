text = input("Введите произвольный текст: ")
replace_input = input("Введите две строки для замены (строка1 строка2): ")
replace_parts = replace_input.split()
if len(replace_parts) != 2:
    print("Ошибка: пожалуйста, введите ровно две строки через пробел")
else:
    old_string, new_string = replace_parts
    formatted_text = text.replace(old_string, new_string)
    print("\nОтформатированный текст:")
    print(formatted_text)