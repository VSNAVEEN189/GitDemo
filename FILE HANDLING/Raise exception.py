# raise 
# if we want to raise error we can
# Exception - all error comes under this\ generic - optional


salary = float(input("Enter salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative")
else:
    print(f"Your salary is {salary}")
    

# custom age message for the error
age = float(input("Enter your age: "))

if age < 0:
    raise ValueError("age cannot be negative")
else:
     if age >= 18:
         print("You can vote")
     else:
          print("You cannot vote")      
        

age = float(input("Enter your age: "))

if age < 0:
    raise Exception("age cannot be negative")
else:
     if age >= 18:
         print("You can vote")
     else:
          print("You cannot vote")      