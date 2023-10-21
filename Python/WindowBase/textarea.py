from tkinter import *

def clickP():
    inputt = text.get('1.0',END)
    print(inputt)

window = Tk()

text = Text(window,
            bg='light yellow',
            font=('Ink free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='dark red')
text.pack()

button = Button(window,command=clickP,text='submit')
button.pack()

window.mainloop()