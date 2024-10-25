string = input("Введите отзыв: ")
splited = string.split(" ")
for i in range(0,len(splited)-1,1):
    if splited[i]=="не" and splited[i+1]=="плохой":
        splited[i]