from abc import ABC, abstractmethod

class Organism(ABC):

    Alive = True

    @abstractmethod
    def Eat(self):
        pass

class Animal(Organism):

    def Eat(self):
        print('Eat')

    def Sleep(self):
        print('sleepin')

class Rabbit(Animal):
    def run(self):
        print('Rabbit runnin')


Rabbit = Rabbit()

