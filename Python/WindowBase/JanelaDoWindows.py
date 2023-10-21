from tkinter import *

window = Tk() #instance new
window.geometry('420x420')
window.title('NOGGERS')

icon = PhotoImage(file='WindowImage.png') # precisa ser .png
window.iconphoto(True,icon)
window.config(background="#ffffff")

Photo = PhotoImage(file='WindowImage.png')

label = Label(window,text='Ola',
              font=('Arial',10,'bold'),
              fg='#201936',
              bg='#ffffff',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=5,
              image=Photo,
              compound='bottom')

label.place(x=50,y=50)
label.pack()

clicks = 0

def click():
    global clicks 
    clicks += 1

    print(clicks)

button = Button(window,text='Solteira?',
                command=click,
                font=('Comic Sans',20,'bold'),
                fg='#201936',
                bg='#ffffff',
                activeforeground='#201936',
                activebackground='#ffffff',
                state=ACTIVE,
                image=None,
                compound='bottom') 
button.pack()

window.mainloop() # place window