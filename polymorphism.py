x="hello world"
print(len(x))
my_tuple=("Apple","mango","banana")
print(len(my_tuple))
dicti={"brand":"ford","model":"mustang","year":"1985"}
print(len(dicti))
#class polymorphism
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move (self):
        print("drive")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move (self):
        print("sail")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move (self):
        print("fly")
car1=Car("ford","mustang")
boat1=Boat("ibiza","touring20")
plane1=Plane("boeing","747")
for x in (car1,boat1,plane1):
       x.move()
#inheritsnce class polymorphism
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move (self):
        print("move")
class car(vehicle):
    pass
class boat (vehicle):
    def move (self):
        print("sail")
class plane(vehicle):
    def move (self):
        print("fly")
car1=car("ford","mustang")
boat1=boat("ibiza","touringzo")
plane1=plane("boeing","747")
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
    