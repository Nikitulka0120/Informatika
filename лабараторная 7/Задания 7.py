import random
import string

itog_string = ""
length = int(input("Введите длину пароля: "))
upers = input("Включить заглавные буквы? (да/нет): ").lower()
if upers == "да":
    itog_string += string.ascii_uppercase

lowers = input("Включить строчные буквы? (да/нет): ").lower()
if lowers == "да":
    itog_string += string.ascii_lowercase

digits = input("Включить цифры? (да/нет): ").lower()
if digits == "да":
    itog_string += string.digits

sepc = input("Включить специальные символы? (да/нет): ").lower()
if sepc == "да":
    itog_string += string.punctuation

if itog_string == "":
    print("Вы не выбрали ни одного типа символов! Попробуйте снова.")
else:
    password = ""
    for i in range(length):
        password += random.choice(itog_string)
    print("Ваш пароль:", password)
