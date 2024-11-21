e_counter=0
e_words=[]
all_words=0
with open('file6.txt', 'r', encoding='utf8') as file:
        record = file.readline()
        while record:
            splited=record.split()
            all_words+=len(splited)
            for word in splited:
                for e_finder in word:
                     if e_finder=='e':
                            e_counter+=1
                            e_words.append(word)
            record = file.readline()
print(*e_words)
print("Всего слов - ", all_words)
print("Слов с буквой e - ", e_counter)
print("Итого % слов с буквой e - ", (e_counter/all_words)*100,"%")