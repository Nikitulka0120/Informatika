age = int(input("Введите возраст попселя: "))
if (age <= 2 and age>0):
    print("Введённый вами год эквивалентен ", age*10.5," человеческим")
elif age>=2:
    print("Введённый вами год эквивалентен ",10.5*2+4*(age-2)," человеческим")
else:
    print("Ошибка!")