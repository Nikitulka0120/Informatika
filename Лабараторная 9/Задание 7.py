n = int(input("Введите количество рядов в зале: "))
friends = int(input("Введите количество необходимых подряд идущих свободных мест: "))

matrix = []
print("Введите состояние зала построчно:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

found = False
for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] == 0:
            count += 1
            if count == friends:
                print(f"\nНомер подходящего ряда: {i + 1}")
                found = True
                break
        else:
            count = 0
    if found:
        break

if not found:
    print("\nФиаско, необходимого ряда не нашлось")
