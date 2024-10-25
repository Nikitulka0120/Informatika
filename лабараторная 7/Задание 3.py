string=input("Введите фразу: ")
arr=list(string)
for i in range(0,len(arr),1):
    if len(arr)==1 or i == len(arr)-1:
        print(arr[i])
    else:
        print(f'{arr[i]}.',end='')
