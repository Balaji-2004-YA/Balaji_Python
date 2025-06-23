#local scope
def my_func():
    x=300
    print(x)
my_func()
#function inside a function
def my_func():
    x=300
    def my_innerfunc():
        my_innerfunc()
my_func()
#global scope
x=300
def my_func():
    print(x)
my_func()
print(x)
