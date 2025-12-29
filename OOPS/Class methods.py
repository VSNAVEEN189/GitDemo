# class methods are defined inside the class that are bound to the class
# to create a class method, we use a decorator ->classmethod

print("-----------CREATING CLASS METHOD-----------")
class Welcome:

    @classmethod
    def greet(cls):
        print(cls)
        print("Hello")

w1 = Welcome()
w1.greet()         # Here the class name is being passed
print(Welcome)

print("--------------------------------------=")
class Student:
    '''
    This is a class student to manage student info and activities
    '''
    college_name = "ABC college"
    departments = ["Arts", "Commerce", "Science"] 

    def __init__(self, name, roll):            
        print(f"Calling the initializer for {self}")
        self.name = name     
        self.roll = roll        
        
    def study(self, n_hours): 
        print(self)
        print(f"self is: {self}")              
        print(f"The student studies for {n_hours} hours a day!")

    def sports(self, sports_name):
        print(f"The student plays {sports_name} in the college {self.college_name}")

    @classmethod
    def greet(cls):
        print(cls)          #cls is the class name itself
        print(f"Welcome to {cls.college_name}")     #to access class variable

    @classmethod
    def get_department(cls):
        print(f"Departmnents in {cls.college_name} are:")  
        for department in cls.departments:
            print(department)  


student1 = Student('John', 1001)    
student1.study(3)    
student1.greet()
student1.sports("Football")
student1.get_department()

# We use classmethod to work with class variable.