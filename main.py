from pytubefix import YouTube
import PySimpleGUI as sg
import subprocess
import sys
import os

def check_dependencies():
    try:
        import PySimpleGUI
        import pytubefix
        print("Dependências já instaladas.")
    except ImportError:
        print("Dependências não encontradas. Instalando...")
        install_dependencies()


def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar dependências: {e}")
        sys.exit(1)


def dowloader():
    #Create interface TELA
    sg.theme("DarkRed1")

    interface = [
        [sg.Titlebar("Youtube DownLoad", "assets/img/yt.png", "white", "gray")],
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
        sg.popup("Download Finished")
        print("Download Finished")

    window.close()
    exit()


if __name__ == "__main__":
    # Verifica se o arquivo 'requirements.txt' está presente no mesmo diretório
    if not os.path.isfile("requirements.txt"):
        print("O arquivo 'requirements.txt' não foi encontrado.")
        sys.exit(1)

    check_dependencies()
    dowloader()
