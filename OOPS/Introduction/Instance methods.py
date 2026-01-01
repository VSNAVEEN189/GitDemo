# objects are called instance of the class 
# instance method - defined inside a class which is bound to/ associated with instance or object

class Student:
    '''
    This is a class student to manage student info and activities
    '''

    def study(self, n_hours): 
        print(f"self is: {self}")              #Self has to be there as argument for any instance method
        print("The student studies for {n_hours} hours a day!")

    def sports(self, sports_name):
        print(f"The student plays {sports_name}")


student1 = Student()
print(f" The object: {student1}")

# Calling instance method
student1.study(3)          #Gives error and says 1 was given
student1.sports("Football")

print("-----------------------------------------------")
student2 = Student()
print(f" The object: {student2}")
student2.study(2)
student2.sports("Tennis")

'''
When we call an instance method using the object/instance of the class, Python passes the object itself
as the first argument to that method.
That first argument is by standard is self.
object itself is getting passed as a first argument needs to be accepted by self argument.

Any method that you create inside the function by default it becomes the instance method
can have n.numbers of instance method inside the class it is also associated with the object when we call the object.

And every instance should have self argument to capture the object by default
'''


