days = int(input("Введите количество дней: "))
hours = int(input("Введите количество часов: "))
mins = int(input("Введите количество минут: "))
sec = int(input("Введите количество секунд: "))
result = days * 86400 + hours * 3600 + mins * 60 + sec
print("Итого:",result)