import random
secret = random.randint(1, 10)
print("Хорошо, я загадал число. Попробуй его отгадать")
counter=1
while 1:
    num = int(input("> "))
    print("Номер попытки:", counter)
    if num == secret:
        print("Поздравляю! Вы угадали! Хотите сыграть ещё?(Введите у)")
        if input()=="y":
            secret = random.randint(1, 10)
            counter=1
        else:
            break
    else:
        print("Нее, ты не угадал. Попробуй снова")
        counter+=1
        if num>secret:
            print("Подсказка: ваше число больше загаданного")
        else:
            print("Подсказка: ваше число меньше загаданного")