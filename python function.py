def my_func():
    print("hrllo from the function")
my_func()
#arguments
def my_func(fname):
    print("my name is",fname)
my_func("john")
my_func("balaji")
my_func("snil")
def my_func(name,age):
    print("hello my name is",name,"and my age is",age)
my_func("balaji","25")
#Arbitary Arguments 
def my_func(*kids):
    print("my youngest child is",kids[1])
my_func("ben","balji","don")
#keyword Arguments
def my_name(fname):
    print("my name is",fname)
my_name(fname="john")
#Arbitary keyword Arguments 
def my_func(**kid):
    print("his last name is",kid["lname"])
my_func(fname="john",lname="balaji")
#default parameter Arguments
def my_country(country="india"):
    print("my country is",country)
my_country("canada")
my_country()
#passing listn of arguments
def my_func(food):
    for i in food:
        print(i)
        print(food)
food=["idli","dosa","poori"]
my_func(food)
food=["idli","dosa","poori"]
for i in food:
    print(i)
    print(food[1])
#return values
def my_func(x):
    return x*3
print(my_func(5))
#recursion
def factorial(n):
    if(n<1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#Lambda function 
x=lambda a: a+10
print(x(5))
y=lambda a,b,c: a*b*c
print(y(3,2,5))
#print the numbers from 1 to 10 using functions
def my_func():
    for  i in range (1,11): 
        print(i)
my_func()
#print even numbers from 1 to 10 using functions
def my_func():
    for i in range(0,21,2):
        print(i)
my_func()