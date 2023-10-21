import pyautogui
import time
import keyboard
from threading import Thread

Points = []

loop = False

while True:

    def move():

        if loop == False:

            for i in Points:
                pyautogui.moveTo(i[0],i[1],duration=1)
                pyautogui.click()
        else:
            while True:

                for i in Points:

                    pyautogui.moveTo(i[0],i[1],duration=.1)
                    pyautogui.click()

                time.sleep(.1)

    if keyboard.read_key().lower() == 'e':
        Points.append(pyautogui.position())
        print(Points)

    if keyboard.read_key().lower() == 'f':
        exit()

    if keyboard.read_key().lower() == 'l':
        loop = not loop
        print(loop)

    if keyboard.read_key().lower() == 'r':
        newthread = Thread(target=move)
        print('send')
        newthread.start()