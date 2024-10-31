message = input("Введите зашифрованное сообщение: ")
new_word = [""] * len(message)

if message[-1] == "#":
    message = message.replace("#", "")
    for i in range(len(message)):
        if i % 2 == 0:
            new_word[i // 2] = message[i]
        else:
            new_word[len(message) - 1 - (i // 2)] = message[i]

    print("".join(new_word))
else:
    print("Нет #")
