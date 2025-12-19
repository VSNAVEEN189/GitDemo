# a mode =>append mode
#  If the file does not exist, 'a' mode creates the file/

fh = open("file4  .txt", 'at')
fh.write("\nThis content has been written using a mode.\n")
fh.write("'a mode creates the file if not already existing.\n")
fh.write("Good bye!")
fh.close()
