from tkinter import *
from time import *
import time

def update():
    time_str = strftime('%I:%M:%S')
    timelabel.config(text=time_str)

    day_str = strftime('%A          %B %d, %Y')
    daylabel.config(text=day_str)

    window.after(1000,update)

window = Tk()

timelabel = Label(window,font=('Arial',50),foreground='black')
timelabel.pack()

daylabel = Label(window,font=('Arial',15),foreground='black')
daylabel.pack()

update()

window.mainloop()