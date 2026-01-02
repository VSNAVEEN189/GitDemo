from my_abstract_class import Shape  #Import abstract class module

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2    
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length* self.breadth
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
print("-------AREA OF SQUARE--------")
sq1 = Square(10)
print(sq1.area()) 
print("-------AREA OF RECTANGLE-------")
r1 = Rectangle(6, 5)
print(r1.area())

print("-------AREA OF CIRCLE--------")
c1 = Circle(10)
print(c1.area())