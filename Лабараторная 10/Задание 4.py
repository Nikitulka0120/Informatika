
def file_opener(filename):
    with open(filename, 'r', encoding='utf8') as file:
        for i in range(n):
            record = file.readline()
            if record:
                human = record.split()
                print(*human[0])
            else:
                print("В файле нет больше данных")
                break
            
n=int(input("Введите количество имен: "))
pol=input("Введите пол (М/Ж): ")
if pol.lower() == "м":
    file_opener("file8.txt")
if pol.lower() == "ж":
    file_opener("file7.txt")

