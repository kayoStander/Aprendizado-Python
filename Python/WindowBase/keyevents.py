from tkinter import *

def Key(key):
    print('pressed: ', key.char)
    label.config(text=key.char)
    #window.quit()

window = Tk()

window.bind('<Key>',Key)

label = Label(window,font=('Helvetica',100))
label.pack()

window.mainloop()