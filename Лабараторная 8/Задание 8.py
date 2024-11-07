n = int(input("Введите количество слов: "))
words = []
for i in range(n):
    word=input("Введите слово: ")
    words.append(word)
for word in words:
    if len(word) > 10:
        a10n = f"{word[0]}{len(word) - 2}{word[-1]}"
        print(a10n)
    else:
        print(word)