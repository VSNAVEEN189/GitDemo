n = 1               #GLOBAL VARIABLE  can be inside the function as well.

def func():
    global n        #to assign value to global variable inside function.
    n = 5           #LOCAL VARIABLE
    print('in', n)

func()

print('out', n)