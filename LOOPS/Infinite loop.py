print("-------While true using for loop if condition is true it breaks the loop ")
correct_password = "Python"

while True:  #infinite loop
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password is Correct! Congrats")
        break
    else:
        print("Wrong password Try Again")
print("Logged in!")

print("---------------Print numbers--------------")
num = 20

while num >= 10:
    print(num)
    num = num - 2