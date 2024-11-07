import random
count = 0
streak = ""  
while True:
    flip = random.choice(["О", "Р"])
    print(flip, end=" ")
    streak += flip
    count += 1
    if streak[-3:] == "ООО" or streak[-3:] == "РРР":
        print(f"\nКоличество подбрасываний: {count}")
        break
