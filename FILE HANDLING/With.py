print("--------WITHOUT WITH STATEMENT-------")
fh = open("file1.txt", "rt")
contents = fh.read()
fh.close()
print(contents)

print("-------WITH STATEMENTS-----")
with open("sample2.txt", "xt") as fh:
    fh.write("New file creation\n")
    fh.write("Bye")

# closes the file automatically if error also
# Xmode can be done first then wmode cannot be exist gives error 