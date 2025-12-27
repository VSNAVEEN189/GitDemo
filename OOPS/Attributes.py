class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "John"                #Created 2 attribute for student1
student1.roll = 1001

print(student1.name)             # Attributes has to be created while objects inside the class
print(student1.roll)             # Attributes are associated with each object

# print(student2.name)
# print(student2.roll)      #Will give attribute error 

help(Student)

print(student1.__dict__)    #Gets variables associate with the objec
# __dict__ Will store the variables or attributes that are associated with the object as a dictionary 