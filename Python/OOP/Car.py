class Car():

    color = None

    def __init__(self):
        Col3or = None

    def turn_On(self):
        print('turned on')

        return self
    
    def Drive(self):
        print('Drivin')

        return self
    
    def Brake(self):
        print(' Breakin')

        return self
    
    def Turn_Off(self):
        print( 'Turnin off')

        return self

car = Car()

def ChangeCarColor(car,color):
    car.color = color

ChangeCarColor(car,'white')

print(car.color)

