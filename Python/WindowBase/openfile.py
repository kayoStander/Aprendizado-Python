from tkinter import *
from tkinter import filedialog
import os

def clickP():
    filepath = filedialog.askopenfilename(title='Please choose a file.',filetypes=(('text files','*.txt'),('all files', '*,*'))) # initialdir='path'
    if os.path.isfile(filepath):
        readable = open(filepath,'r')
        print(readable.read())

window = Tk()

button = Button(window,text='open',command=clickP)
button.pack()

window.mainloop()