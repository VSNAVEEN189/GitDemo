# a = 10 
# b = 20
# print(a + b) # a.__add__(b) a dot dunder add is called with b.

# class A:
#     def f1(self, val):
#         pass

# obj =A()
# obj.f1(20)  
# We cannot use + operator without __add__ in any class.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __add__(self, other):   #Magic method
        return self.length + other.length      # r1.length + r2.length


r1 = Rectangle(5, 3)
r2 = Rectangle(8, 6) 
print(r1.area())
print(r2.area())

print(r1 + r2)       # Rectangle.__add__(r1, r2)
# help(int)

# Operator overloading is polymorphism where operators -  
# behave differently depending on the object they’re used with.

# Operator overloading is *a way to give operators 
# (+, -, , ==, etc.) different meanings for different objects.