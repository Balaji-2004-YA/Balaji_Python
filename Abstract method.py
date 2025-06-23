from abc import ABC,abstractmethod
# Abstract Class 
Classshape(ABC)
@abstractmethod
def area (self):
    pass
@abstractmethod
def perimeter (self):
    pass 
# subclass implementing Abstractmethod
class Rectangle(shape):
    def __init__(self,width,heighgt):
        selfwidth=width
        selfwidth=heighgt
    def area (self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width+self.height)
#using Abstractmethod class rect=rectangle (4,5)
print("area:","rect.area()")
print()