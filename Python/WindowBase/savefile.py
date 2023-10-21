from tkinter import *
from tkinter import filedialog

def clickP():
    filer = filedialog.asksaveasfile(defaultextension='.txt',
                                     filetypes=[('.TEXT FILE','.txt'),('.HTML FILE','.html'),('ALL FILES','.*')]
                                        ,)

    if filer is None:
        return
    
    filetext = str(text.get(1.0,END))
    #filetext = input('enter text: ')

    filer.write(filetext)
    filer.close()

window = Tk()

button = Button(window,text='confirm',command=clickP)
button.pack()

text = Text(window)
text.pack()

window.mainloop()