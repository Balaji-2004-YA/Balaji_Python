##1).[python Variables]
#strings:
name="balaji"
print(name)
my_car="benz"
print(my_car)
##integer
age=50
print(age)
kilometer=1542
print(kilometer)
##float
Range=50.36
print(Range)
##2).Multiple variables
a,b,c=10,20,30
print(a)
print(b)
print(c)
Name,age,village=("balaji",25,"yandrikayalapalli")
print(name)
print(age)
print(village)
##3).reassiging variables
age = 25
print(age) 
age = 30
print(age) 
##4).Dynamic Typing
value=46
print(type(value))
name="balaji"
print(type(name))
#Data Types
##1: Integer (int)
num1 = 10
print(type(num1))  # Output: <class 'int'>
##2: Floating-point (float)
num2 = 3.14
print(type(num2))  # Output: <class 'float'>
##3:Complex (complex)
num3 = 2 + 3j
print(type(num3))  # Output: <class 'complex'>
## 5: List (list)
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>
##Tuple (tuple)
coordinates = (10, 20, 30)
print(type(coordinates))
##Dictionary (dict)
person = {"name": "John", "age": 30}
print(type(person))  # Output: <class 'dict'>
##Set (set)
fruits_set = {"apple", "banana", "cherry"}
print(type(fruits_set))  # Output: <class 'set'>
##Boolean (bool)
is_sunny = True
print(type(is_sunny))  # Output: <class 'bool'>
##None (NoneType)
nothing = None
print(type(nothing))  # Output: <class 'NoneType'>
##len function it is used to get how many charecters are there in a srting
a="hi balaji how are yo"
print(len(a))
v="hi balaji how are yo"
print(v.upper())
Name="balaji"
Age=65
print(f"my name is {name},and my asge is {Age}")
names=["balaji","sunil","gone"]
names.insert(2,"hiva")
print(names)
names=["balaji","sunil","gone"]
names.insert(1,"hiva")
print(names)
names=["balaji","sunil","gone"]
morenames=["care","haei"]
print(names.extend(morenames))
print(names)
morenames=["care","haei"]
morenames.append("balaj")
print(morenames)
###loops
fruits = ["apple", "banana", "cherry"]
for a in fruits:
    print(a)
for i in range (5):
    print(i)
count=0
while count >5:
    print(count)
   