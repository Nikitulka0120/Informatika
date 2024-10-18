arr=[]
started=True
control=2
while(started):
    height = int(input("Введите рост человека:"))
    if (height != 0 and height>0):
        arr.append(height)
    elif (len(arr)<control and height==0):
        print("Некого сравнивать")
        started=False
    elif (height==0):
        print("Ввод завершён")
        started = False
if (len(arr)>=control):
    print("Самый высокий человек:",max(arr))
    print("Самый низкий человек:",min(arr))