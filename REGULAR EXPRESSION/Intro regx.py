# Regular expression(Regx) built in module 
# a special sequence of character that defines a pattern for doing complex string matching functionality.
# re module provides a series of metacharacters or special symbol and quanatifiers to create the patterns for serching.
print("----NORMAL WAY TO FIND SUBSTRING-----")
message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."

# if Python is present in message
print("Python" in message)
print("13" in message)
print("14" in message)

print(message.find('3.13'))
print(message.find("Python"))

print("-----REGX MODULE(RE)-----")
import re 

# re.serach(regx_pattern, string) 
# => it returns a match object when there is a match found, else returns None
# Match obj to find where the match is 
# re.search helps to find pattern in the string first occurence only,

message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."

match_obj = re.search('13', message)
print(match_obj)

if re.search('13', message):
     print("Found!")
else:
     print("Not found!")    

print(message[32:34])     