def main_compact():
    import string
    print("Введите текст (пустая строка для завершения):")
    word_count = {}
    while True:
        line = input()
        if line == "":
            break
        translator = str.maketrans('', '', string.punctuation + string.digits + '—–«»„“”')
        clean_line = line.translate(translator)
        words = clean_line.lower().split()
        for word in words:
            if word:
                word_count[word] = word_count.get(word, 0) + 1
    if word_count:
        print("\nСтатистика слов:")
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    else:
        print("Нет данных для анализа")