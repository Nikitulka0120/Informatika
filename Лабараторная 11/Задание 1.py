phone_dic={'.,?!:':'1',
           'abc':'2',
           'def':'3',
           'ghi':'4',
           'jkl':'5',
           'mno':'6',
           'pqrs':'7',
           'tuv':'8',
           'wxyz':'9',
           ' ':'0',
           }
text = input("Введите текст: ")
for letter in text.lower():
    for button in phone_dic:
        if letter in button:
            pos=button.find(letter)
            for k in range(pos+1):
                print (phone_dic[button], end='')
