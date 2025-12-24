import re 

message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."
print("----THE DIGIT-----")
match_obj = re.search("[0-9][0-9]", message)   #Square bracket anyone character between them
print(match_obj)

match_obj = re.search("[0-9][0-9][0-9]", "House number: 251/A")   #Square bracket anyone character between them
print(match_obj)

# . dot - matches any character except new line character (\n) a special character 
print("----DOT .----")

match_obj = re.search("[0-9].[0-9][0-9]", message)
print(match_obj)

match_obj = re.search("[0-9].[0-9]", message)
print(match_obj)

match_obj = re.search("[0-9].[0-9]", "House number: 251/A")   
print(match_obj)

message_1 = "The year is 2011"
match_obj = re.search("[0-9].[0-9][0-9]", message_1)
print(match_obj)

match_obj = re.search("[0-9][.][0-9][0-9]", message_1)
print(match_obj)

match_obj = re.search("[0-9][.][0-9][0-9]", message)
print(match_obj)