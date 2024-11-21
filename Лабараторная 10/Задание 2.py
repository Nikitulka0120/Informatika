def finder(filename):
    with open(filename, 'r', encoding='utf8') as file:
        record = file.readline()
        while record:
            if " Academy" in record:
                return True
            record = file.readline()
if finder("file5.txt"):
    print("В 5 файле")
elif finder("file6.txt"):
    print("В 6 файле")
