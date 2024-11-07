rost = list(map(int, input("Введите рост пиплисов: ").split()))
andruha = int(input("Введите рост Андрюхи: "))
rost.sort(reverse=True)
pos = 1
for height in rost:
    if height < andruha:
        break
    pos += 1

print("Андрей должен встать на позицию:", pos)