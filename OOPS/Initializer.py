# __init__() method 
# Is an instance method - is used to create and initialise attributes durinig the creation of the object
# It's a special method 

class Student:
    '''
    This is a class student to manage student info and activities
    '''

    def __init__(self, name, roll, dept):            #By default by python
        print(f"Calling the initializer for {self}")
        self.name = name     #This both are instance variable
        self.roll = roll        # 2 attributes will be created for each of the object will be created.
        self.department = dept 
    def study(self, n_hours): 
        print(f"self is: {self}")              #Self has to be there as argument for any instance method
        print("The student studies for {n_hours} hours a day!")

    def sports(self, sports_name):
        print(f"The student plays {sports_name}")

student1 = Student("john", 1001, "Science")              # Object creation    
# object_name.attribute_name = value

student2 = Student("Carol", 1002, "Arts")     #This should be created inside the class with some value.

print(student1.name, student1.roll, student1.department)
print(student2.name, student2.roll, student2.department)

# to check the attribute
print(student1.__dict__)
print(student2.__dict__)

# Instance variables/attributes are different for different objects

# to add an attribute in object separately
student1.grade = "B"
print(student1.__dict__)
print(student2.__dict__)

student3 = Student("Alice", 1003, "Science")
print(student3.__dict__)

# All the attributes or the variable should be define inside the __init__ only 