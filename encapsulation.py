class MyClass:
    def _init_(self, name):
        self.name = name  # Public attribute
        self._age = 30    # Protected attribute (convention)
        self.__salary = 50000  # Private attribute (name mangling)

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self._salary}")

    def __private_method(self):
        return "This is a private method"

# Creating an instance of MyClass
obj = MyClass("Alice")

# Accessing public attribute
print(obj.name)  # Output: Alice

# Accessing protected attribute (not enforced, but discouraged)
print(obj._age)  # Output: 30

# Attempting to access the private attribute directly (will raise AttributeError)
# print(obj.__salary) # Uncommenting this will raise an error

# Accessing private attribute using name mangling
print(obj.MyClass_salary)  # Output: 50000

# Attempting to access the private method (will raise AttributeError)
# print(obj.__private_method())  # Uncommenting this will raise an error

# Accessing private method using name mangling
print(obj.MyClass_private_method())  # Output: This is a private method