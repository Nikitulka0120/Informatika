digits = []
min_digits=[]
max_digits=[]

while 1:
    digit = input()
    if digit != "":
        digits.append(int(digit))
    else:
        break

avg=float(sum(digits)/len(digits))
for i in range(len(digits)):
    if digits[i]>avg:
        max_digits.append(digits[i])
    else:
        min_digits.append(digits[i])
print("AVG ",avg)
print("Bolshe ",*max_digits)
print("Menshe",*min_digits)

