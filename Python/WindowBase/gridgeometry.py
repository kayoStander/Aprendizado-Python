from tkinter import *

def clickP():
    pass

window = Tk()

text = Label(window,text='enter your info').grid(row=0,column=0,columnspan=2)

firstnamelabel = Label(window,text='first name: ',width=20).grid(row=1,column=0)
firstnameentry = Entry(window).grid(row=1,column=1)

lastnamelabel = Label(window,text='last name: ').grid(row=2,column=0)
lastnameentry = Entry(window).grid(row=2,column=1)

emailnamelabel = Label(window,text='email name: ').grid(row=3,column=0)
emailnameentry = Entry(window).grid(row=3,column=1)

button = Button(window,text='Confirm',command=clickP).grid(row=4,column=0,columnspan=2)

window.mainloop()