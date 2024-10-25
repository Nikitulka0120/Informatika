string=input("Введите фразу:")
splited=string.split(" ")
if len(splited)==2:
    perev = splited[::-1]
    for i in perev:
        print(i, end=" ")
else:
    print("Ошибка")