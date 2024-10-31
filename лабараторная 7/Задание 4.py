otziv = input("Введите отзыв: ")

otziv = otziv.lower().replace("не плохой", "хороший")
otziv = otziv.lower().replace("не плоха", "хороша")
otziv = otziv.lower().replace("не плохо", "хорошо")

print("Исправленный отзыв:", otziv)