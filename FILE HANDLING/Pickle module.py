# Pickle - list set tuples dict when we want to store this data types in 
# files they need to be converted in sequence of bit that computer can 
# understand is called serialisation

# To access in original data type is deserialization

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 71.0}}

print(students)
print(type(students))


with open("students_info.txt", "w") as fh:
    fh.write(str(students))


with open("students_info.txt", "rt") as fh:
    content = fh.read()

print(type(content))    
# Can't print back dict from the text file once converted to string.
out = dict(content)
print(out)

# to access to read back the data
# pickle.dump()                      #To dump the content of the file

import pickle

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 71.0}}

print(students)
print(type(students))

# Serialization
# Opening the file in binary using bx, used for loop and dump fuction 
# to dump content one by one as file holder.

with open("students.bin", "bw") as fh:         #file exist so w instead of x.
    for student in students: 
        pickle.dump(students[student], fh)


# Deserialization - Reading back data from the file in origianl format

with open("students.bin", "rb") as fh:
    data1 = pickle.load(fh)
    print(data1, type(data1))
    data2 = pickle.load(fh)
    print(data2, type(data2))
    data3 = pickle.load(fh)
    print(data3, type(data3))

# When file is exhausted we get eoferror: Ran out of input doen't how much data is stored   