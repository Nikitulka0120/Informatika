n = int(input("Введите количество комнат: "))
count = 0
for _ in range(n):
    p, q = map(int, input("Введите текущее и максимальное количество людей в комнате: ").split())
    if q - p >= 2:
        count += 1

print(count)