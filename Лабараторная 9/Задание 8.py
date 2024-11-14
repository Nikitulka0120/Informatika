n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(0)
    matrix.append(line)
for i in range(n):
    print (*matrix[i])
print ("\n")

for i in range(n):
    for j in range(m):
        if (i==0):
            matrix[i][j]=1
        else:
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for i in range(n):
    print (*matrix[i])