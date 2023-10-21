import pyautogui
import time
import keyboard

print(pyautogui.size())

start = input('Start? Y/N ').lower()

def play():
    pyautogui.moveTo(x=1270,y=680,duration=0)
    pyautogui.click()
    pyautogui.moveTo(x=1060,y=400,duration=0)
    pyautogui.click()
    pyautogui.moveTo(x=1350,y=350,duration=0)
    pyautogui.click()
    pyautogui.dragTo(x=1350,y=400,duration=.5)
    pyautogui.moveTo(x=1080,y=620,duration=0)
    pyautogui.click()

if start == 'y':

    time.sleep(4)

    while True:
        if keyboard.read_key().lower() != 'p':
            play()
        else:
            exit()

else:
    exit()

print(pyautogui.position())