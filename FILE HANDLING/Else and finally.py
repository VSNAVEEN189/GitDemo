print("----BASIC TRY AND EXCEPT-----")
try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()

    print(data)    
except FileNotFoundError:
    print("File that you are trying to open does not exist!")

print("--------TO SHOW THE MESSAGE-------")
try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()

    print(data)    
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print(file_err)

# else - when there is no error happens in try block no exception
# To display the contents of the file
print("----ELSE----")
try:
    with open("file1.txt", "rt") as fh:
        data = fh.read() 
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print(file_err)
else: 
    print(data)

# Finally
print("-----FINALLY----") 
import io
try:
    fh = open("file10.txt", "wt")    
    data = fh.read() 
    fh.close()
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)    
else: 
    print("else block")
    print(data)
finally:
    print("Finally block")     
    fh.close()
# when no error it goes to else block and finally block
# we have to close the file

print("-----FINALLY=-1-----") 
import io
try:
    fh = open("file10.txt", "wt")    
    fh.write("Hello")
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)    
else: 
    print("else block")
    # print(data)
finally:
    print("Finally block")     
    fh.close()