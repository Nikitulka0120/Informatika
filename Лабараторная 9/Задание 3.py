import math

min_distance = float('inf')
min_dist = None
sanek = input("Введите координаты Александра: ")
sasha_x, sasha_y = map(int, sanek.split())

n = int(input("Введите количество сундуков: "))
treasures = []

print("Введите координаты сундуков:")
for i in range(n):
    point = input().split()
    x, y = int(point[0]), int(point[1])
    treasures.append((x, y))


for x, y in treasures:
    distance = math.sqrt((x - sasha_x) ** 2 + (y - sasha_y) ** 2)
    if distance < min_distance:
        min_distance = distance
        min_dist = (x, y)

print(f"Координаты ближайшего сокровища: {min_dist}")