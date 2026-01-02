class SalaryError(Exception):
    pass


def get_salary(salary):
    if salary < 0:
        raise SalaryError("Salary cannot be negative")
    else:
        bonus = 0.1 * salary 
        return salary + bonus
    

salary = int(input("Enter your salary: "))    
final_salary = get_salary(salary)
print(final_salary)

###
# Transaction
