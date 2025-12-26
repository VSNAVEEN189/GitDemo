import re

print("------SUB()------")
# substituting sub()
# Used to replace a pattern to get a new pattern, 
#  replacing some characters, abbrevations, words to some other words, unwanted.

s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = "Sunday"
replacement = "friday"

result = re.sub(pat, replacement, s1, count=1)
print(result)

s1 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = r"S[a-z]+"
replacement = "friday"
result = re.sub(pat, replacement, s1)
print(result)

message = "We are learning re. using re, we can search for a pattern in a given string." \
"Using the sub(), we can replace the pattern with a given string as well."

pat = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(pat, replacement, message)
print(result)

print("-----BOTH CAPITAL RE AND small re-----")
message = "We are learning re. using RE, we can search for a pattern in a given string." \
"Using the sub(), we can replace the pattern with a given string as well."

pat = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(pat, replacement, message, flags=re.IGNORECASE)
print(result)

print("------REPLACING (+,-)------")
phone_nums = "+91-1234567890, +91-9999999999"
pattern = r"[+-]"
replacement = ""
result = re.sub(pattern, replacement, phone_nums)
print(result)

print("------compile------")
# compiles the pattern object and that is further used in place of raw string pattern.
# For using multiple times it's helpful for time optimization.

phones = "Alice-1234567890, Mark-9876543212, Carol-1290875673"

pattern = r"\d{10}"
match_obj = re.findall(pattern, phones)
print(match_obj)


pattern = r"\d{10}"
pattern_compile = re.compile(pattern)

print(pattern_compile)
print(type(pattern_compile))

match_obj = re.findall(pattern_compile, phones)
print(match_obj)

with open("student_details", "rt") as fh:
    data = fh.read()

print(data)
print(type(data))    

phone_matches = re.finditer(pattern_compile, data)
print(phone_matches)

for matches in phone_matches:
    print(matches)