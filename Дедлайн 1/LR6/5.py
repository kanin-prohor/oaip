text = input("Введите произвольный текст: ")
search_word = input("Введите слово для поиска: ")
word_count = text.count(search_word)
first_index = text.find(search_word)
text_without_word = text.replace(search_word, "")
print(f"\nРезультаты поиска слова '{search_word}':")
print(f"Количество встреченных слов: {word_count}")
if first_index != -1:
    print(f"Индекс первого встреченного слова: {first_index}")
else:
    print("Слово не найдено в тексте")
print(f"\nТекст без слова '{search_word}':")
print(text_without_word)