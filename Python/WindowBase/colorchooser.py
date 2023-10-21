from tkinter import *
from tkinter import colorchooser

def clickP():
    window.config(background=colorchooser.askcolor()[1])

window = Tk()

button = Button(window,text='click',command=clickP)
button.pack()


window.geometry('420x420')
window.mainloop()