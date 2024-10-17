# AAA777
# 5555FFF
while True:
    znak = str(input("Введите номерной знак формата ААА000 или 0000ААА:"))
    std="unstd"
    if len(znak) == 6:
        std="old"
        for i in range(3):
            if znak[i].isdigit()==False:
                continue
            else:
                std="unstd"
            if znak[2+i].isdigit:
                continue
            else:
                std="unstd"

    elif len(znak) == 7:
        std="new"
        for i in range(4):
            if znak[i].isdigit:
                continue
            else:
                std="unstd"
            if znak[3+i].isdigit==False:
                continue
            else:
                std="unstd"

    match std:
        case "old":
            print("Знак древний, выкинуть пора")
        case "new":
            print("Классный новый свежий знак")
        case "unstd":
            print("Что вы мне втюхать пытаетесь?")
