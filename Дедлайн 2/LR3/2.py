text = input("Введите произвольный текст: ")
char_count = {}
for char in text:
    lower_char = char.lower()
    char_count[lower_char] = char_count.get(lower_char, 0) + 1
print("\nРезультат подсчета символов:")
for char, count in char_count.items():
    print(f"'{char}': {count}")