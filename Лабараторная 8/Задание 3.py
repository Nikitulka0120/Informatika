mass = input("Введите строку чисел:").split(" ")
new_mass=[]
for i in range (0,len(mass)-2):
    if mass[i]<mass[i+1]:
        print(mass[i+1], end=" ")
