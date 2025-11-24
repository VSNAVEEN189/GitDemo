#Area of the triangle
"""
semi perimeter(s) = (a+b+C)/2
Area = square root of (s *(s-a) * (s-b) * (s-c))

a = float(input("Enter first side: "))
b = float(input("Enter first side: "))
c = float(input("Enter first side: "))
s = (a+b+c)/2
area = (s *(s-a) * (s-b) * (s-c)) ** 0.5
print("The area of the triangle with given side is", round(area, 2))
"""

#Simple interest
"""
Simple interrest = (P + R+ T)/100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interst rate: "))
Time = float(input("Enter the time: "))  
SI = (principal + rate + Time)/100
print("Simple interest is", SI)
"""

#Compound interest
"""
Amount = P(1 + R/100) ** T
CI = Amount - P

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time: "))
#amount1 = principal * (1 + rate / 100) ** time
amount2 = principal * pow((1 + rate / 100), time)
print(round(amount2, 2))
ci = amount2 - principal
print("Compound interest", ci)
"""
