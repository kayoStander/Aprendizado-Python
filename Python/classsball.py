class ball():
    
    def __init__(self,canvas,x,y,diameter,xVEL,yVEL,Color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=Color)
        self.xVelocity = xVEL
        self.yVelocity = yVEL

    def Move(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[2]>=self.canvas.winfo_width() or coordinates[0]<0:
            self.xVelocity = -self.xVelocity
            
        if coordinates[3]>=self.canvas.winfo_height() or coordinates[1]<0:
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)