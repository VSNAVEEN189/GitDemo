# java-script object notation provides a utility to handle data is widely used in text based format in data exchange
# json handle with json library with .json used in api and data storage 
# Every boolean is in lower case and key values are in double quoted".

print("----IMPORTING JSON CREATING FILE----")
import json 

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 98.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 92.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 81.5}}

print(students)
print(type(students))

# dump() - dictionary into proper json file

with open("student.data.json", "w") as fh:
    json.dump(students, fh, indent=4)



import json 

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 95.5, 'sports': True},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 92.5, 'sports': False},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 85.5, 'sports': True}}

print(students)
print(type(students))

print("------DUMP-----")
# dump() - dictionary into proper json file

with open("student.data.json", "w") as fh:
    json.dump(students, fh, indent=4)

print("----LOAD----")
# Load()- for reading the file

with open("student.data.json", "r") as fh:
    data = json.load(fh)

print(data)
print(type(data))

# update - adds new data in the json file, File has to be present
# First load the file and read it then update it

print("-----UPDATE when file present----")
# read the old data from the json file
with open("student.data.json", "r") as fh:
    data = json.load(fh)
    
#update operation 
data.update(students)

# dump - write the updated data in the json file
with open("student_data.json", 'w') as fh:
    json.dump(data, fh, indent=4)

print("----when file not present----")

try: 
    # read the old data from the json file
    with open("student.data.json", "r") as fh:
        data = json.load(fh)
except FileNotFoundError:  
    with open("student_data.json", 'w') as fh:
        json.dump(students, fh, indent=4)
else:        
       # #update operation 
    data.update(students)
    # # dump - write the updated data in the json file
    with open("student_data.json", 'w') as fh:
     json.dump(data, fh, indent=4)
