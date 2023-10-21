from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')

notebook.pack(expand=True,fill='both') # expand  = expand to fill any space not otherwise used, # fill = will fill in x and y 

label1 = Label(tab1,text='hello tab 1',height=25,width=50).pack()
label2 = Label(tab2,text='hello tab 2',height=25,width=50).pack()

window.mainloop()