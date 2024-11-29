n = int(input("Введите количество членов экипажа: "))
first=[]
second=[]
for i in range(n):
    chlen = input("Введите имя и статус (woman/child/man/captain)")
    temp = chlen.split(" ")
    if temp[1].lower()=="woman" or temp[1]=="child":
        first.append(temp[0])
    elif temp[1].lower()=="man":
        second.append(temp[0])
    else:
        cap=temp[0]

def print_chlens(category):
    for i in category:
        print(i)

print_chlens(first)
print_chlens(second)
print(cap)