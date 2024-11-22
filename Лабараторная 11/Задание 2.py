points={'aeilnorstu':1,
           'dg':2,
           'bcmp':3,
           'fhvwy':4,
           'k':5,
           'jx':8,
           'qz':10,
           }
total_score=0
text = input("Введите слово: ")
for letter in text.lower():
    for point in points:
        if letter in point:
            total_score+=points[point]
print(total_score)
