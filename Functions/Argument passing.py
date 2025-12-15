#  In python , we can pass function as a argument of another function.

def add_1(number):
    return number + 1

print(add_1(10))


def square(number):
    return number ** 2

num = int(input("Enter a number:"))
res_1 = add_1(num)
res_2 = square(res_1)
print(f"Output is: {res_2}")


# Instead of doing one by one.
def square(number):
    return number ** 2

num = int(input("Enter a number:"))
res = square(add_1(num))       #Passing the function call itself.
                               #Multiple function calls can be passed as arguments.
print(f"Output is: {res}")