import PySimpleGUI as sg
from random import randint
points={'aeilnorstu':1,
           'dg':2,
           'bcmp':3,
           'fhvwy':4,
           'k':5,
           'jx':8,
           'qz':10,
           }
sg.theme('GrayGrayGray')
layout = [
    [sg.Text("Игра эрудит", justification="center")],
    [sg.Text("Введите слово:"), sg.InputText(key="word")],
    [sg.Button("Подсчитать очки", button_color=("white", "#4B0082"))],
    [sg.Text("Результат:"), sg.InputText(key="result", readonly=True)],
    [sg.Image("erudit.png", size=(300, 300), visible=True, key="image_placeholder")],
]


window = sg.Window("Эрудит", layout, size=(500, 500), element_justification="center", finalize=True)
while True:
    total_score=0
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Подсчитать очки":
        try:
            text = str(values["word"])
            for letter in text.lower():
                for point in points:
                    if letter in point:
                        total_score += points[point]
            window["result"].update(total_score)
        except ValueError:
            sg.popup_error("Ошибка", "Введите корректные числовые значения!")

window.close()



