# Module - .py file is a module include functions, states, classes, etc. of its own
# to group functions for better code organization and reusability.
# built in modules: math, random, datetime, os, sys, etc.
# how to import a module:
# syntax: import module_name
# syntax : for importing only few functions/variables: from module_name import f1, f2, f3.

print("--------Importing math module--------")
import math
# calculate square root of a number
num = 100
output = math.sqrt(num)   #module.function_name
print(f"The square root of {num} is {output}")

print("--------Area of circle using math module---------")
# Calculate the area of a circle
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is {area_of_circle}")
print(math.pi)

print("-------Using random module------")
# Throw a die 
from random import randint
value = randint(1, 6)  # generates a random integer between 1 and 6
print(f"You rolled a die and got: {value}")

print("--------Using datetime module creating an alias-------")
# syntax to create an alias for the module that is being imported: import module_name as alias_name  
import datetime as dt
t = dt.time(8, 44, 51)
print(t)