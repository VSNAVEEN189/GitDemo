# The programming which is oriented toward objects 
# class is design or blueprint, objects are actual product. hepls to write code better way
'''
# object - kind of container
        data  = attributes
        fuctionality = methods\behaviour

'''

fruits = ["mango", "apple", "orange"]
print(type(fruits))

# fruits is an object of a class 
fruits.append("grapes")           #It is a method or behaviour were i can add more fruits in the list
print(fruits)

"""
car1
     => brand = "BMW", model = "XYZ340", year = 2020    #data
     => accelerate, brake,                              #Functionality

dot notation  (.)

car1.brand => "BMW"
car1.accelerate(10)                 #Methods are just nothing but function
"""

# Creating objects

# calsses => templates\blueprints\design used for creating objects
# also called as type

# objects are created using the classes
# Instances of a class 
# We can create multiple objects using single class

# CREATING CLASS

class MyClass:
    pass                               # to make tactical correct for empty class 

# Creating object
obj1 = MyClass()
obj2 = MyClass()

# obj1 and obj2 are objects of class MyClass

l1 = [10, 20, 30]
print(type(l1))

print(type(obj1))
print(type(obj2))     #-- -- any thing with double underscore front and back is dunder

# Methods - the functions that are defined inside the class , Any functions that is defined inside a class is method.
# Calling methods using objects?
# obj1.method(arg1, arg2,...)

class Student:
    """
    This is a class student to manage student information and activities
    """
    pass

s1 = Student()
s2 = Student()

# Doc string of a class is the details of a class basically the documentation
print(Student.__doc__)

print(help(Student))         #To get the documentation of the class 2nd method.