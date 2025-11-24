#Slicing of string
"""
Syntax of indexing: string[index]
Syntax of slicing: string[start:end:step]
start: starting index at which the slicing operation starts
end: ending index at which the slicing stops (excluded)
step: integer that specifies the step for the slicing
"""

s1 = "Hello World"
#print(s1[2:9:2])
#print(s1[1:12:3])
s1_slice = s1[1:12:3]
print(s1_slice)
print(type(s1_slice))