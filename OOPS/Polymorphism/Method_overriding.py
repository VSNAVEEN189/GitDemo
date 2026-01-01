# Method that is being inherits by child class might not behave the same way as parent class.
# We can change the behaviour of method that is being inherit from parent class it can be done by redefining
# the method in child class this process is-called method overriding.

class Employee:
    def working_hours(self):
        return 45
    

class Intern(Employee):
    def working_hours(self):
        return 40

i1 = Intern()
print(i1.working_hours())

# If i don't want same behaviour as parent class to be in for child class 
# for that we create a method in child class