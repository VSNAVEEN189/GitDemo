"""Recursion is a process in which a function calls itself till a certain conditon is not met.
Factorial of a number => n*(n-1)*(n-2)*.....*1
n!
4! = 4 * 3 * 2 * 1 = 24
n! => n * (n-1) * (n-2) * .... * 2 * 1
   => n * (n-1)!    
   => n * (n-1) * (n-2)! .....
"""

print("-------------Without recursion-------------")
def fact(num):
    factorial = 1
    while num >= 1:
        factorial *= num
        num -= 1

    return factorial    

n = 5
print(f"Factorial of {n} is {fact(n)}")

# There are 2 parts to any recursive function
# 1. Base/terminal condition - It should stop calling itself . 
# 2. Recursive condition - 
# Useful for problems which can be broken down into smaller sub-problems of the same type. 
# To keep calling itself with modified arguments.

print("-------------With recursion-------------")
def fact_rec(num):
    # Base condition
    if num == 1:
        return 1                            #Factorial of 1 is 1
    else:
        factorial = num * fact_rec(num - 1)  # Recursive condition
        return factorial
    
print(fact_rec(4))   