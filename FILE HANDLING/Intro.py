# File handling refers to the process of performing operations on a file, 
# such as creating, opening, reading, writing and closing it through a programming interface

# Modes: r, x, w, a, t, b, 
# r  - read, x  - create, w  - write, a  - append, t  - text mode, b  - binary mode

print("--------OPENING AND CLOSING A FILE--------")
# opening a file 
file = open("sample.txt", 'rt') 
# print(file)
# # closing a file
# file.close()

print("------Read operation------")
# read() => reads the entire content of the file as a string.

# content = file.read()
content = file.read(10)   # This reads first 10 characters of the file.
# readline() => reads a single line from the file.
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()   # Empty string as end of file reached
line5 = file.readline()
# readlines() => reads all lines and returns a list of lines

# closing a file => close()
lines = file.readlines()  # reads all lines and returns a list of lines

file.close()

print(f"lines: {line1}")
print(f"type of lines: {type(line1)}")

for line in line1:
    print(line.strip())   # strip() removes extra new line characters from the line.
