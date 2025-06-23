class person:
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
p1=person("john",25,21-25-2004)
print(p1.name)
print(p1.age)
print(p1.dob)
#class attribute and instance attribute
class car:
    wheels=8
    def __init__(self,colour):
        self.colour=colour
c1=car("red")
c2=car("blue")
print(c1.wheels)
print(c2.wheels)
print(c1.colour)
print(c2.colour)
c1.colour="green"
print(c1.colour)
print(c2.colour)
#object methods 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_fun(self):
            print("hello,my name is" + self.name)
p1=person("john",26)
p1.my_fun()
p1.name="ben"
p1.my_fun()
class Animal:
     species="mammal"
     def __init__(self,name):
          self.name=name
dog=Animal("dog")
cat=Animal("cat")
print(dog.species)
print(cat.species)
print(dog.name)
print(cat.name)
Animal.species="bird"
print(dog.species)
print(cat.species)
dog.name="bulldog"
print(dog.name)
print(cat.name)
dog.age=5
print(dog.age)

 