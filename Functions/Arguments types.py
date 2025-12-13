def add(a, b):
    return a + b

# Positional arguments- Passing arguments in order of their positions
result = add(10, 5)

print("------------ Default Arguments -----------")
# Default arguments - we can assign value to one or more argument
# The first value becomes optional value has to present for both Has a defautl argument thats a optional argument
# the non-default arguments should not follow the default argument positional argument should not come before the default argument

def add(a, c, b=10,):
    print(f"a: {a}, b: {b}, c: {c}")                  #Gives an parameter error
    return a + b + c

result = add(10, 5)
print(result)                                                                    

# result = add(10)
# print(result)

result = add(10, 20, 30)
print(result)

print("------------ Keyword Arguments -----------")
# Keyword argument 
def add(a, c, b=10,):
    print(f"a: {a}, b: {b}, c: {c}")              #argument values can be in any order
    return a + b + c

result = add(10, c=50)                           # b will be default value, used to call the function
print(result)                                    #We have to give atleast one value


print("------------ Variable Length Arguments -----------")
# Variable length argument----*args - Star number of argument(0 to n) variable length positional
def add(*args):
    print(args, type(args))                     #args is a tuple

add(10, 20, 4, 1, 3, 5, 7)    
#args is a standard name, we can use any name with star symbol like nums or x. y, z.

def add(*args):
    return sum(args)                               # No star symbol needed while using sum function

result = add(10, 20, 4, 3, 5, 7) 
print(result)

print("------------EXAMPLE-------------")
def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid}) was absent in all the exams")
    else:    
         percent = sum(marks) / len(marks)
         print(f"{sname} with id {sid} secured {percent}%")

student_details(101, "John", 87.0, 69.5, 81.5, 74.0)
student_details(102, "Carol", 91.0, 49.5, 91.5, 84.0, 86.5)
student_details(104, "Alice")