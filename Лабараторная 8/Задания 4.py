digits = []
min_digits=[]
max_digits=[]
result = list(map(int, digits))
while 1:
    digit = input()
    if digit != "":
        digits.append(digit)
    else:
        break
avg=int(sum(result)/len(result))
for i in range(len(result)):
    if result[i]>avg:
        max_digits.append(result[i])
    else:
        min_digits.append(result[i])
print(avg)
print(*max_digits)
print(min_digits)

