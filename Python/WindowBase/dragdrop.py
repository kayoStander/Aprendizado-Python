from tkinter import *

def dragstart(key):
    widget = key.widget
    widget.startX = key.x
    widget.startY = key.y

def dragmotion(key):
    widget = key.widget
    x = widget.winfo_x() - widget.startX + key.x
    y = widget.winfo_y() - widget.startY + key.y

    widget.place(x=x,y=y )



window = Tk()

label = Label(window,bg='blue',width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg='red',width=10,height=5)
label2.place(x=100,y=0)

label.bind('<Button-1>',dragstart)
label.bind('<B1-Motion>',dragmotion)

label2.bind('<Button-1>',dragstart)
label2.bind('<B1-Motion>',dragmotion)

window.mainloop()