from tkinter import *

def clickP():
    #w = Toplevel()
    w = Tk()

    window.destroy()

    w.mainloop()

window = Tk()

button = Button(window,text='create a window',command=clickP).pack()

window.mainloop()