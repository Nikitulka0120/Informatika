result = input("Введите результаты матча: ")
score = result.split(" ")[-1:]
teams = result.replace(score[0],"")
teams=teams.split("-")
score=score[0].split(":")
if int(score[0])>int(score[1]):
    print("Поздравим %s" %(teams[0]))
elif int(score[0])<int(score[1]):
    print("Поздравим %s" %(teams[1]))
else:
    print("Ничья")