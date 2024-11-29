import PySimpleGUI as sg
from random import randint
sg.theme('DarkPurple')
layout = [
    [sg.Text("Генератор случайных чисел", justification="center")],
    [sg.Text("Введите нижнюю границу:"), sg.InputText(key="lower")],
    [sg.Text("Введите верхнюю границу:"), sg.InputText(key="upper")],
    [sg.Button("Сгенерировать", button_color=("white", "#4B0082"))],
    [sg.Text("Результат:"), sg.InputText(key="result", readonly=True)],
    [sg.Image("dice_PNG23.png", size=(1000, 1000), visible=True, key="image_placeholder")],
]


window = sg.Window("Рандом", layout, size=(400, 300), element_justification="center", finalize=True)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Сгенерировать":
        try:
            lower = int(values["lower"])
            upper = int(values["upper"])
            if lower > upper:
                sg.popup_error("Ошибка", "Нижняя граница не может быть больше верхней!")
            else:
                random_number = randint(lower, upper)
                window["result"].update(random_number)
        except ValueError:
            sg.popup_error("Ошибка", "Введите корректные числовые значения!")

window.close()
