from tkinter import *
from tkinter import filedialog
import os

def Create():

    def clickP():
        filer = filedialog.asksaveasfile(defaultextension='.txt',
                                     filetypes=[('.TEXT FILE','.txt'),('.HTML FILE','.html'),('ALL FILES','.*')]
                                        ,)
        if filer is None:
            return
    
        filetext = str(text.get(1.0,END))

        filer.write(filetext)
        filer.close()

    CreateWindow = Toplevel() 
    CreateWindow.title('Create a file')

    button = Button(CreateWindow,text='Send',command=clickP)
    button.pack()

    text = Text(CreateWindow,
                height=20,
                width=50)
    text.pack()

    CreateWindow.mainloop()

def Read():

    def clickP():
        filepath = filedialog.askopenfilename(title='Please choose a file.',filetypes=(('text files','*.txt'),('all files', '*,*'))) # initialdir='path'
        if os.path.isfile(filepath):
            readable = open(filepath,'r')
            text.delete(1.0, END) 
            text.insert(1.0 , str(readable.read()))

        

    CreateWindow = Toplevel() 
    CreateWindow.title('Read a file')

    button = Button(CreateWindow,text='Choose one file to read',command=clickP)
    button.pack()

    text = Text(CreateWindow,
                height=20,
                width=50)
    text.pack()

    CreateWindow.mainloop()

window = Tk()
window.title('Menu')

imageidk = PhotoImage('placeholder')

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=('My Boli',9))
menubar.add_cascade(label='File',menu=filemenu)    #image=photoimageidk,compound='right')
filemenu.add_command(label='Create',command=Create)
filemenu.add_command(label='Read',command=Read)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=quit)

editmenu = Menu(menubar,tearoff=0,font=('My Boli',9))
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='PLACEHOLDER',command=lambda : print('hi'))

window.mainloop()