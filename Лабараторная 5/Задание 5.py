while True:
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    if a+b>c and a+c>b and b+c>a:
        if (a == b and b == c):
            print("Треугольник равносторонний")
        elif (a == b or b == c or c == a):
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольника не существует")