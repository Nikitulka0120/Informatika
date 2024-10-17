
a = int(input("Введите трехзначное число: "))

sotni = a // 100
desyatki = (a // 10) % 10
edenici = a % 10
sum = sotni + desyatki + edenici
print("Сумма:", sum)
