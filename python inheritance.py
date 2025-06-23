class Animal:
    def speak(self):
        return"Animal"
class Dog(Animal):
    def bark (self):
         return "woof!!"
Dog=Dog()
print(Dog.speak())
print(Dog.bark())
#multiple inheritance
class bird:
    def fly(self):
        return"flies high"
class swimmer:
    def swim(self):
        return"swims well"
class duck(bird,swimmer):
    pass
duck=duck()
print(duck.fly())
print(duck.swim())

class Vehicle:
    def drive(self):
        return"driving"
class car(Vehicle):
    def fuel (self):
        return"runs on fuel"
class electicalcar(car):
    def charge (self):
        return"charging battery"
tesla=electicalcar()
print(tesla.drive())
print(tesla.fuel())
print(tesla.charge())

class Device:
    def power_on(self):
        return"device"
class Computer(Device):
    def compu(self):
        return"computer initized"
class Laptop (Computer):
    def portable (self):
        return"laptop is portable"
laptop=Laptop()
print(laptop.power_on())
print(laptop.compu())
print(laptop.portable())
comp= Laptop()
print(comp.power_on())
print(comp.compu())
print(comp.portable())
class Animal:
    def breath(self):
        return"breathing"
class Dog:
    def meow(self):
        return"meow"
class Cat (Animal):
    def woof (self):
        return"woof"
dog=Dog()
cat=Cat()
print(Dog.breath())
print(cat.breath())
#hybrid inheritance