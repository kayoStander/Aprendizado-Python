from tkinter import *
import time
import classsball

window = Tk()

WIDHT,HEIGHT=500,500

canvas = Canvas(window,width=WIDHT,height=HEIGHT)
canvas.pack()

volleyball = classsball.ball(canvas,0,0,100,1,1,'green')
mickeyball = classsball.ball(canvas,0,0,50,3,4,'black')
sleepball = classsball.ball(canvas,0,0,10,2,5,'red')
worldball = classsball.ball(canvas,0,0,250,11,5,'blue')

while True:
    volleyball.Move()
    mickeyball.Move()
    sleepball.Move()
    worldball.Move()
    window.update()
    time.sleep(.01)

window.mainloop()