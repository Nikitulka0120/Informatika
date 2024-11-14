import random

# Вводим размерность матрицы
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        value = random.randint(0, 10)
        row.append(value)
    matrix.append(row)

tmatrix = []
for j in range(m):
    trow = []
    for i in range(n):
        trow.append(matrix[i][j])
    tmatrix.append(trow)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Транспонированная матрица:")
for row in tmatrix:
    print(row)
