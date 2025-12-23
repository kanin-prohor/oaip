text = input("Введите текст: ")
letters = 0
digits = 0
punctuation = 0
spaces = 0
punctuation_marks = ".,!?:;"
i = 0
while i < len(text):
    char = text[i]
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char in punctuation_marks:
        punctuation += 1
    elif char == ' ':
        spaces += 1
    i += 1
print(f"Буквы: {letters}")
print(f"Цифры: {digits}")
print(f"Знаки препинания: {punctuation}")
print(f"Пробелы: {spaces}")