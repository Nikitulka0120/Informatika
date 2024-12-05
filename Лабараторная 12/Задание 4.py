import PySimpleGUI as sg

def binus(number):
    binary = '00000000'
    if number >= 0:
        sign_bit = '0'
    else:
        sign_bit = '1'
    number = abs(number)
    bin_form = f'{number:07b}'
    binary = sign_bit + bin_form
    
    return binary

def reverce(binary):
    reverse_code = binary[0]
    
    for bit in binary[1:]:
        if bit == '0':
            reverse_code += '1'
        else:
            reverse_code += '0'
    return reverse_code

def adit(binary):
    reverse_code = reverce(binary)
    sign_bit = reverse_code[0]
    ad_code = sign_bit + f'{int(reverse_code[1:], 2) + 1:07b}'
    return ad_code

def check(fun):
    try:
        number = int(values["INPUT"])
        if -128 <= number <= 127:
            if fun == binus:
                binary_code = fun(number)
            else:
                binary_code = fun(binus(number))
            
            window["RESULT"].update(f"Результат: {binary_code}")
        else:
            sg.popup("Ошибка", "Диапазон от -128 до 127")
    except ValueError:
        sg.popup("Ошибка", "Введите корректное число.")

layout = [
    [sg.Text("Введите число (-128 до 127):"), sg.Input(key="INPUT", size=(10, 1))],
    [sg.Button("Прямой код"), sg.Button("Обратный код"), sg.Button("Дополнительный код")],
    [sg.Text("Результат:", size=(10, 1)), sg.Text("", key="RESULT", size=(40, 1))],
]

window = sg.Window("Кодирование чисел", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Прямой код":
        check(binus)
    elif event == "Обратный код":
        check(reverce)
    elif event == "Дополнительный код":
        check(adit)

window.close()
