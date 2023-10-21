from tkinter import *

def move(key):

    amt = 10

    print(key.char)

    if key.char == 'w':
        canvas.move(label,0,-amt)
    elif key.char == 'a':
        canvas.move(label,-amt,0)
    elif key.char == 's':
        canvas.move(label,0,amt)
    else:
        canvas.move(label,amt,0)

window = Tk()
window.geometry('500x500')

keys = ['w','a','s','d']    

for i in keys:
    window.bind('<'+i+'>',move)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

label = canvas.create_rectangle(0,0,50,50)

window.mainloop()