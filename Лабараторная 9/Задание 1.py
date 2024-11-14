def func(x):
    return x**2 / (10 + x**3)
a = -2
b = 5
n = 10000
h = (b - a) / n
f = []
i = a
while i < b:
    f.append(func(i))
    i += h
sum = 0
for i in range(1,len(f)-1):
    sum += f[i] * h
sum += (a + b)/2 * h
print(f"{sum:.2f}")