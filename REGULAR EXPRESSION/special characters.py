import re
# # To create a pattern we use r 

# s1 = "Python is a programming language"

# # [A-Z], [a-z]
# pat = r"old\new"
# print(pat)
# pat = r"[A-Z][a-z][a-z]"
# match_obj = re.search(pat, s1)
# print(match_obj)

# print("-----d and D-----")
s2 = "Python is a programming Language. python3.13 is the current version."
# # \d and \D
# # \d matches 1 digit character. It is similar to [0-9]. followed by digit only 
# pat = r"[a-z][a-z][a-z]\d"
# match_obj = re.search(pat, s2)
# print(match_obj)

# # \D matches 1 non-digit character. It is similar to [0-9]. Doesn't follow by any digit
# pat = r"[a-z][a-z][a-z]\D"
# match_obj = re.search(pat, s2)
# print(match_obj)

print("----s, S----")
# \s,\S
# \s matches any whitespace character. tab and new line also.
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s2)
print(match_obj)

s3 = """Hi there
We are learning python
"""
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s3)
print(match_obj)

# \S opposite of \s .It matches any character except, space, \n and \t
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat, s3)
print(match_obj)

print("----W, w----")
# \w - matches [a-z], [A-Z], [0-9], 
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat, s3)
print(match_obj)

# \W- Exact opposite of \w - matches a character except [a-z], [A-Z], [0-9] should not be a alphanumeric
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat, s3)
print(match_obj)