fh = open("my_program.py", "rt")
contents = fh.read()
fh.close()

print(contents)  #If file not present gives an error at output.

fh = open("file1.txt", "rt")
fh.write("Some content")
fh.close()    #Two modes cannot be done at once.
# cannot use this type of function.
