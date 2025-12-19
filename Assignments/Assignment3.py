print("-------TASK 1------")
# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number
number = 6

# Function call
fact = factorial(number)

# Printing the output
print("Factorial of", number, "is:", fact)


print("-------TASK 2-------")
import math

# Ask the user for a number
num = int(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display the results
print("Square root:", square_root)
print("Natural logarithm:", natural_log)
print("Sine (in radians):", sine_value)
