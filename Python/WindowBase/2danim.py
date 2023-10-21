from tkinter import *
import time

WIDHT,HEIGHT = 500,500

XVEL,YVEL = 1,1 

window = Tk()

canvas = Canvas(window,width=WIDHT,height=HEIGHT)
canvas.pack()

photo = PhotoImage('WindowImage.png')

canv = canvas.create_image(0,0,Image=photo,anchor=NW)

IMAGEWIDHT,IMAGEHEIGHT = canv.widht(),canv.height()

while True:
    coordinates = canvas.coords(canv)
    print(coordinates)
    if coordinates[0] >= IMAGEWIDHT or coordinates[0] <=0:
        XVEL = -XVEL
    if coordinates[1] >= IMAGEHEIGHT or coordinates[1] <=0:
        XVEL = -XVEL
    canvas.move(canv,XVEL,0)
    window.update()
    time.sleep(.01)

window.mainloop()
