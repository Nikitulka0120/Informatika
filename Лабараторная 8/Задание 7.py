card = list(map(int, input("Введите номер карты: ")))
total_sum = 0

for i in range(len(card)):
    num = card[i]
    if i % 2 == 0:
        doubled = num * 2
        if doubled > 9:
            doubled -= 9
        total_sum += doubled
    else:
        total_sum += num

if total_sum % 10 == 0:
    print("класс")
else:
    print("не класс")