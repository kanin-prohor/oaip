text = input("Введите текст: ").lower()
words = set(text.split())

print(f"Уникальных слов: {len(words)}")

print("Слова длиннее 5 символов:")
long_words = [w for w in words if len(w) > 5]
print(long_words if long_words else "Нет таких слов")

if "python" in words or "programming" in words:
    print("Есть ключевые слова!")
else:
    print("Ключевых слов нет")