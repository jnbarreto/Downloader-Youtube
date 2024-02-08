import PySimpleGUI as sg
from pytube import YouTube

#Create interface TELA
sg.theme("Dark Blue 16")

interface = [
    [sg.Titlebar("Youtube DownLoad", None, "white", "gray")],
    [sg.Text("URL")],
    [sg.Input(size=(50,1), key="url")],
    [sg.Button("Download")]
]

window = sg.Window("window", interface)

while True:
    event, value = window.read()

    if value == sg.WIN_CLOSED:
        break

    if event == 'Download':
        link = window["url"].get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution().download()
    print("Download Finished")

window.close()
exit()