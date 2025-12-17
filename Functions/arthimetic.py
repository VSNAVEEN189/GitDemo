# A simple arithmetic module: arthimetic.py



def add(num1, num2):
    return num1 + num2


def square_root(num):
    return num ** 0.5

print(f"__name__value in arthimetic.py => {__name__}")

# __name__ variable
if __name__ == "__main__":    #To make 30 not visible in mycode.py while importing
    a = 10
    b = 20
    result = add(a, b)
    print(result)

# helps when we want to run some code only when the module is run directly, not when it is imported.    