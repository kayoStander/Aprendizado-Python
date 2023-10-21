from tkinter import *
from tkinter.ttk import * 
import time

def clickP():
    while progressbar['value']<100:
        time.sleep(.05) 
        progressbar['value'] += 1
        porcentl.set(str(progressbar['value'])+'%')
        window.update_idletasks()

window = Tk()

porcentl = StringVar()

progressbar = Progressbar(window,orient=HORIZONTAL,length=300)
progressbar.pack(pady=10)

porcent = Label(window,textvariable=porcentl).pack()

button = Button(window,text='Download',command=clickP).pack()

window.mainloop()