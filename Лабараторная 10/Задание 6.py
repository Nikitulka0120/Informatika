processed_lines=[]
def reverse_words_in_file(input_filename, output_filename):

    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        words = line.split()
        reversed_words = [word[::-1] for word in words]
        processed_line = ' '.join(reversed_words)
        processed_lines.append(processed_line)
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_lines))
filename=input("Введите название файла")
reverse_words_in_file(filename, "new_file.txt")