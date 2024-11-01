
spisok = input("Введите строку: ").split(" ")
string=[]
digits=[]
for i in spisok:
    if i.isdigit():
        digits.append(i)
    else:
        string.append(i)
print("Цифры:",*digits)
print("Строки:",*string)
