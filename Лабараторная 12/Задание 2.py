stringa=input("Введите: ")
if stringa[0]=="q":
    if stringa.lower().count("q") == stringa.lower().count("a"):
        print("+")
    else:
        print("-")
else:
    print("Вопрос должен быть первым")