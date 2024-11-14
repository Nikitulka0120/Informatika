n = int(input("Введите размер матрицы: "))
matrix = []
print("Введите элементы матрицы построчно:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

print("Изменённая матрица:")
for row in matrix:
    print(" ".join(map(str, row)))
