text = input().replace(',', ' ').replace('.', ' ')
words = [w for w in text.split() if w]

vowels = set('аеёиоуыэюяaeiouy')

upper_count = 0
vowel_end_count = 0
longest_word = ""

for word in words:
    if word[0].isupper():
        upper_count += 1
    if word[-1].lower() in vowels:
        vowel_end_count += 1
    if len(word) > len(longest_word):
        longest_word = word

print(f"С заглавной: {upper_count}")
print(f"Оканчиваются на гласную: {vowel_end_count}")
print(f"Самое длинное слово: {longest_word}")