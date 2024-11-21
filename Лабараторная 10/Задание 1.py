winner = ""
max_score = 0
with open('file4.txt', 'r', encoding='utf8') as file:
    record = file.readline()
    while record:
        human = record.split()
        if int(human[-1]) > max_score:
            second_place=winner
            second_score=max_score
            winner = human[0] + " " + human[1]
            max_score = int(human[-1])
            
        record = file.readline()
print("Призер:", second_place, " ( Набранное количество баллов:", second_score, ')')
