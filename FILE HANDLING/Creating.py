print("--------CREATING A FILE--------")
# x mode => create a file       

fh = open("file1.txt", 'xt')

# Writing into the file
# write(content)
fh.write("This is created using x mode.\n") 
fh.write("Next line.")

# closing the file
fh.close()          #After closing the file gets closed.
# fh.write("Test content.")  Gives error as file is closed now.

# w mode- open the file for writing .overwrites the file.
# Creates the file if it does not exist.
# If the file exists, it overwrites the file. 

print("------W MODE-----")
fh = open("file2.txt", 'w')
fh.write("This file is created using w mode in python.\n")
fh.write("Have a nice day!")
fh.close()

