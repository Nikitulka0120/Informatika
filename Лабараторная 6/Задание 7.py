s=input("Введите номер билета:")
if len(s)==6:
    if int(s[0])+int(s[1])+int(s[2])==int(s[3])+int(s[4])+int(s[5]):
        print("Ваш билет - счастливый")
    else:
        print("Ваш билет - обычный")
else:
    print("Некорректный билет")