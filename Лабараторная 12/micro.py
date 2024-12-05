import PySimpleGUI as sg
import random as rd

c_image = [[sg.Image("bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Делитель:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="multi")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    micro = int(value["micro"])  #здесь хранится количество бактерий изначально
    count = int(value["count"])  #здесь хранится количество секунд для которых требуется рассчитать
    k=int(value["multi"])
    res = 0                 #здесь будет храниться результат
    x=micro

    for i in range(count):
        b = rd.randint(0, 4)
        x = k * x + b
    res = x

    if event == "Рассчитать":
        window["res"].update(res)


window.close()

