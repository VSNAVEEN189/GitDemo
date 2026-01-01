# We create a method that can be called in different ways
# If we call function add with 2 arguments the first add will be called
# With 3 arguments 2nd one will be called 
# If there are 2methods the latest will be called because its override

class A:
    def add(self, num1, num2):
        return num1 + num2
    

    def add(self, num1, num2, num3):
        return num1 + num2 + num3    # This one will be called
    

obj = A()
print(obj.add(10, 20, 30))    