import re
from collections import Counter

text = input("Введите текст: ")
words = re.findall(r'\b\w+\b', text.lower())

if words:
    print(f"Слов: {len(words)}")
    print(f"Самое длинное: '{max(words, key=len)}'")
    print(f"Самое короткое: '{min(words, key=len)}'")
    print(f"Средняя длина: {sum(len(w) for w in words)/len(words):.1f}")
    
    common = Counter(words).most_common(5)
    print("Частые слова:")
    for word, count in common:
        print(f"  {word}: {count}")