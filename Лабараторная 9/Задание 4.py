menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

while True:
    mode = int(input("Выберите опцию:\n"
                     "1) Отобразить меню\n"
                     "2) Найти блюдо по названию и отобразить его ингредиенты и цену\n"
                     "3) Добавить новое блюдо в меню\n"
                     "4) Изменить цену блюда\n"
                     "0) Выйти\n\n"))
    match mode:
        case 1:
            print("Меню ресторана:")
            for i in menu:
                print(f"{i[0]} - {i[2]} рублисов")
            print("\n")
        case 2:
            bludo = input("Введите название блюда: ")
            for i in menu:
                if i[0].lower() == bludo.lower():
                    print(f"Состав: {', '.join(i[1])}")
                    print(f"Цена: {i[2]} рублисов")
                    break

        case 3:
            name = input("Введите название нового блюда: ")
            ingredients = input("Введите ингредиенты: ").split(" ")
            price = int(input("Введите цену блюда: "))
            menu.append([name, ingredients, price])
            print(f"Блюдо '{name}' добавлено в меню.\n")

        case 4:
            bludo = input("Введите название блюда для изменения цены: ")
            for i in menu:
                if i[0].lower() == bludo.lower():
                    new_price = int(input(f"Введите новую цену для '{i[0]}': "))
                    i[2] = new_price
                    print(f"Цена блюда '{i[0]}' обновлена до {new_price} рублисов\n")
                    break

        case 0:
            print("Выход успешен")
            break

        case _:
            print("Такой опции нет.\n")
