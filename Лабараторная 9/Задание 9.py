import random
matrix=[]
secret_matrix=[]
boats_counter=4
game_status=True
def matrix_fill(mat):
    for i in range(4):
        line = []
        for j in range(4):
            line.append(".")
        mat.append(line)

def boats_and_bombs():
    boat_counter=0
    while boat_counter<4:
        i=random.randint(0, 3)
        j=random.randint(0, 3)
        if secret_matrix[i][j]==".":
            secret_matrix[i][j]="К"
            boat_counter+=1
    
    while True:
        i=random.randint(0, 3)
        j=random.randint(0, 3)
        if secret_matrix[i][j]==".":
            secret_matrix[random.randint(0, 3)][random.randint(0, 3)]="В"
            break


matrix_fill(secret_matrix)
matrix_fill(matrix)
boats_and_bombs()

print("Секретная информация от нашей разведки, сделайте вид что ничего тут нет")
for i in range(4):
    print (*secret_matrix[i])
print ("\n")

while game_status:
    cords = list(map(int, input("Отдайте приказ, Капитан!").split()))
    if secret_matrix[cords[0]-1][cords[1]-1]==".":
        print("Мимо")
        matrix[cords[0]-1][cords[1]-1]="#"
    elif secret_matrix[cords[0]-1][cords[1]-1]=="К":
        print("Попал")
        matrix[cords[0]-1][cords[1]-1]="X"
    elif secret_matrix[cords[0]-1][cords[1]-1]=="В":
        print("Вы проиграли")
        matrix[cords[0]-1][cords[1]-1]=":("
        game_status=False

    for i in range(4):
        print (*matrix[i])
    print ("\n")

