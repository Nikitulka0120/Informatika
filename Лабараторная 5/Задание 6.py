while True:
    month=input("Введите название месяца: ")
    _31=["январь", "март", "май", "июль", "август", "октябрь", "декабрь"]
    _30=["апрель", "июнь", "сентябрь", "ноябрь"]
    _289=["февраль"]
    if month.lower() in _31:
        print("В этом месяце 31 день")
    elif month.lower() in _30:
        print("В этом месяце 30 дней")
    elif month.lower() in _289:
        print("В этом месяце 28 или 29 дней")
    else:
        print("Это че за месяц?")
