import pickle

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 98.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 71.0}}

print(students)
print(type(students))


# Serialization
with open("students.bin", "bw") as fh:         
    for student in students: 
        pickle.dump(students[student], fh)

# Deserialization 
print("----To get the file content using try and except using break----")
with open("students.bin", "rb") as fh:
    while True:
        try: 
            data = pickle.load(fh)
            print(data, type(data))
        except EOFError :
            print("done")
            break
# EOFError: Ran out of input   

print("-----Print the names of the students as a list who secured 90 or more----")
# only print the student name
student_list_90 = []
with open("students.bin", "rb") as fh:
    while True:
        try: 
            data = pickle.load(fh)
            if data['percent'] >= 90:
                student_list_90.append(data['name'])
        except EOFError :
            print("done")
            break

print(f"List of students who secured 90 or more are: {student_list_90}")

# If we dont know how many times should i load data we can use while loop.
