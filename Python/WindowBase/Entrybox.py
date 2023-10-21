from tkinter import *

window = Tk()

entry = Entry(window,
              font=('Arial',50),
              show='')

entry.pack(side=LEFT)

def submitP():
    User = entry.get()
    if len(User) >= 5:

        print('hello ',User)
        entry.config(state=DISABLED)

    else:

        print(' Too short name')


def deleteP():
    entry.delete(0,END)

def backspaceP():
    entry.delete(len(entry.get())-1,END)

submit = Button(window,text='Submit',command=submitP)
submit.pack(side=RIGHT)

delete = Button(window,text='Delete',command=deleteP)
delete.pack(side=RIGHT)

backspace = Button(window,text='Backspace',command=backspaceP)
backspace.pack(side=RIGHT)

window.mainloop()