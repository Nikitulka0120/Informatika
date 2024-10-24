dec=0
step=0
bi=input("Введите двоичное число: ")
for i in range((len(bi)-1),-1,-1):
    if (bi[i]=="1"):
        dec=dec+2**step
    step+=1
print(dec)
