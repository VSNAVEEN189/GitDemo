# Static method - defined inside a class which is neither bound to the object or to the class, to create we use decorator @static method 
class Student:
    '''
    This is a class student to manage student info and activities
    '''
    college_name = "ABC college"
    departments = ["Arts", "Commerce", "Science"] 

    def __init__(self, name, roll):            
        self.name = name     
        self.roll = roll        
        
    def study(self, n_hours):            
        print(f"{self.name} studies for {n_hours} hours a day!")

    def sports(self, sports_name):
        print(f"The student plays {sports_name} in the college {self.college_name}")

    @staticmethod
    def greet():
        print("Welcome to college")     #to access class variable

    @classmethod
    def get_department(cls):
        print(f"Departmnents in {cls.college_name} are:")  
        for department in cls.departments:
            print(department)  

# help(Student)
student1 = Student("John", 1001)
student1.study(3)
student1.get_department()
student1.greet()

student1 = Student("Carol", 1002)
student1.study(2)