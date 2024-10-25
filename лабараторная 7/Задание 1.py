strings = str(input())
spis=strings.split(" ")
k=len(spis)
for i in range(0,len(spis)-2,1):
    if spis[i] == spis[i+1]:
        print(spis[i])
        spis.pop(i+1)
    if i == (len(spis)-2):
        break
for i in spis:
    print(i, end=" ")

# Довольно распространённая ошибка ошибка это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод