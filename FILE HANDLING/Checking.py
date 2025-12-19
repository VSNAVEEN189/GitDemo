# os.path.exists()
print("-----os.path.exists()--------")
import os

file_name = "D:\CODING VS CODE\PYCHARM\FILE HANDLING\With.py"

if os.path.exists(file_name):
    print("file exists")
else:
    print("file doesn't exist")


# pathlib.path.exists()
print("-------path;ib.path.exists()----------")
from pathlib import Path

file_name = Path("D:\CODING VS CODE\PYCHARM\FILE HANDLING\file1.txt")

if file_name.exists:
    print("file exists. Cannot create")
else:
    print("file doesn't exist, Creating it")
    fh = open(file_name, 'xt')
    fh.write("Some content")
    fh.close()