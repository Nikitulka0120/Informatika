def add_line_to_middle(filename, new_line):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    middle_index = len(lines) // 2
    lines.insert(middle_index, new_line + '\n')
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

new_line = input("Введите строку для добавления в середину файла: ")

add_line_to_middle("file4.txt", new_line)
