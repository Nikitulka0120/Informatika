n=int(input())
count=1
m=n
for k in range(n-1):
    for i in range(m-1):
        print(" ", end="")
    for j in range(count):
        print("#", end="")
    count+=2
    m-=1
    print("")
for i in range(n-1):
    print(" ", end="")
print("#", end="")