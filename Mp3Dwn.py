import pyautogui as robot
import time

Navegador = input("Que navegador usas 🐱‍👤?")
Cancion = input("Que cancion deseas descargar 🔊???" + "  Si puedes especificar artista y cancion, aun mejor uwu: ")
YoutubeBar = 530, 131
VideoP = 445, 325
barraMp3 = 633, 342
descargarMp3 = 572, 338

def abrir (pos, click = 1):
    robot.moveTo(pos)
    robot.click(clicks=click)

robot.hotkey("Win","s")
time.sleep(1)
robot.typewrite(Navegador)
time.sleep(0.5)

robot.hotkey("enter")
time.sleep(2)

robot.hotkey("alt","space")
time.sleep(1)
robot.hotkey("x")
time.sleep(1)

robot.hotkey("ctrl","l")
robot.typewrite("youtube.com")
robot.hotkey("enter")
time.sleep(5)

#Cancion = input("Que cancion deseas descargar 🔊???" + "  Si puedes especificar artista y cancion, aun mejor uwu: ")

abrir(YoutubeBar, click=1)
time.sleep(2)
robot.typewrite(Cancion)
robot.hotkey("enter")
time.sleep(3)

abrir(VideoP, click=1)
time.sleep (3)

robot.hotkey("ctrl","l")
robot.hotkey("ctrl","x")
robot.typewrite("https://ytmp3.cc/youtube-to-mp3/")
robot.hotkey("enter")
time.sleep(3)

abrir(barraMp3, click=1)
robot.hotkey("ctrl","v")
robot.hotkey("enter")
time.sleep(4)
abrir(descargarMp3, click=1)
abrir(descargarMp3, click=1)
time.sleep(3)
robot.hotkey("ctrl","shift","w")

