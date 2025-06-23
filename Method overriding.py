class Animal:
    def sound (self):
        return"Animal sound"
class Dog (Animal):
    def sound(self):
        return"bark"
dog=Dog()
print(dog.sound())
class Animal:
    def sound (self):
        return"Animal sound"
class Dog (Animal):
    def sound(self):
        return super().sound()+" and bark"
dog=Dog()
print(dog.sound())
