from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
#blue = canvas.create_line(0,0,500,500,fill='blue',width=5)
#red = canvas.create_line(500,0,0,500,fill='red',width=5)
#canvas.create_rectangle(50,50,250,250,fill='purple',width=5)
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill='yellow',width=5,outline='black')
canvas.create_arc(0,0,500,500,style=PIESLICE,fill='red',start=0,extent=180,width=10)
canvas.create_arc(0,0,500,500,style=PIESLICE,fill='white',start=180,extent=180,width=10)
canvas.create_oval(190,190,310,310,fill='white',width=10)
canvas.pack()

window.mainloop()