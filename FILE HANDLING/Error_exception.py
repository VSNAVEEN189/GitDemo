# Compile time error - syntax and indentation error
# Exception - errors during execution 

age = 24
if age >= 18:
   print("You are an adult")  

x = 100
# result = x + y

# How to handle exceptions? - try-except block 

# This method takes zero division error
print("---ZERO DIVISION ERROR----")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("The denominator cannot be zero")

# another method for accepting value error
print("----VALUE ERROR-----")
try:                                        #Means gives one try
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
    print(result)
except ZeroDivisionError:                    #If not this than this
    print("The denominator cannot be zero")    #If zero is entered
except ValueError:
    print("Input should only be digits")      #If digits are not entered