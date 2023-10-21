from tkinter import *

def display():
    if (x.get()==True):
        print('agree')
    else:
        print('desagree')

window = Tk()

x = BooleanVar()

image = PhotoImage(file='WindowImage.png')

Checkbutton = Checkbutton(window,
                          text='i agree to kirby',
                          variable=x,
                          onvalue=True,
                          offvalue=False,
                          command=display,
                          font=('Comic Sans ', 25),
                          image=image,
                          compound='top')

Checkbutton.pack()

window.mainloop()