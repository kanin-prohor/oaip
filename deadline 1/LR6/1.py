fio_input = input("Введите ваше ФИО через пробел: ")
fio_parts = fio_input.split()
if len(fio_parts) != 3:
    print("Ошибка: пожалуйста, введите Фамилию, Имя и Отчество через пробел")
else:
    formatted_fio = []
    for part in fio_parts:
        if part:
            formatted_part = part[0].upper() + part[1:].lower()
            formatted_fio.append(formatted_part)
        else:
            formatted_fio.append("")
    result_fio = " ".join(formatted_fio)
    print(f"Добро пожаловать, {result_fio}!")