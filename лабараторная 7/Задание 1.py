strings = str(input())
spis=strings.split(" ")
k=len(spis)
i=0
while i < len(spis) - 1:
    if spis[i].lower() == spis[i + 1].lower():
        spis.pop(i + 1)
    else:
        i += 1 
for i in spis:
    print(i.lower(), end=" ")

# Довольно распространённая ошибка ошибка это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод