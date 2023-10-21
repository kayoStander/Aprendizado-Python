from tkinter import *

window = Tk()
window.config(background='#eccbf7')

def submitP():
    print('the temp is', scale.get())

highimage = PhotoImage(None)
highlabel = Label(image=highimage)
highlabel.pack()

scale = Scale(window,from_=100
              ,to=0,
              length=400,
              orient='horizontal',
              font=('Comic Sans',5),
              tickinterval=10,
              showvalue=True,
              resolution=5,
              troughcolor='#8b32a8',
              bg='#eccbf7',
              fg='#bf6fd9'
              )
scale.pack()
scale.set(50)

button = Button(window,text='Submit',command=submitP)
button.pack(side='right')

lowimage = PhotoImage(None)
lowimage = Label(image=lowimage)
lowimage.pack()

window.mainloop()