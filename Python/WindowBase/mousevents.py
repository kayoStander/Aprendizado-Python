from tkinter import *

def Key(key):
    print(key)

window = Tk()

window.bind('<Button-1>',Key) #Enter,#Leave,#ButtonRelease,#Button-2,#Button-3,#Motion

window.mainloop()