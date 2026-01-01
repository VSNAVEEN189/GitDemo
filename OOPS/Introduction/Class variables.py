# Class variables are defined at the class level. 
# same copy of the class variables are shared among the objects


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
        print(f"self is: {self}")              
        print("The student studies for {n_hours} hours a day!")

    def sports(self, sports_name):
        print(f"The student plays {sports_name}")


student1 = Student("John", 1001)

help(Student)
print(student1.__dict__)

print(student1.departments)     # student1 Object
print(student1.college_name)
print(Student.departments)      # Student class
print(Student.college_name)

student2 = Student("Carol", 1002)
print(student2.departments)     # object 
print(student2.college_name)