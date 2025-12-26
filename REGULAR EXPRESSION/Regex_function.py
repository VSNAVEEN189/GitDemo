# match() - focus only on first occurences.
import re
s1 = "We are learning regex in Python"
pat = r"[A-Z][a-z]"
match_obj = re.match(pat, s1)
print(match_obj)

# re.search - will find first occurences 
phones = "1234567890, carol-9021276829, Mark-9326232739"
pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj)

print("------findall()-----")
# findall() - to find all the matches 
phones = "1234567890, carol-9021276829, Mark-9326232739"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)

phones = "1234567890, carol-9021276829, Mark-9326232739, Alice-3434340, Python3.13.5"
pat = r"[0-9]+"                   # This means one or more
match_obj = re.findall(pat, phones)
print(match_obj)

print("----find valid mobile numbers----")
# fetch all phone numbers , the phone numbers are exactly 7 digits and should not exceed 15 digit.
pat = r"[0-9]{7,15}"                #To just find valid mobile numbers 
match_obj = re.findall(pat, phones)
print(match_obj)

print("-----7 or more-----")
# fetch all phone numbers , the phone numbers are atleast 7 digits.
pat = r"[0-9]{7,}"                #7 or more
match_obj = re.findall(pat, phones)
print(match_obj)

phones = "1234567890, carol-9021276829, Mark-9326232739, Alice-3434340, Python3.13.5, Dan-123456789987654321"
pat = r"[0-9]{7,}"                #7 or more
match_obj = re.findall(pat, phones)
print(match_obj)

print("----(-\b) Word boundary------")
# \b - Word boundary
pat = r"[0-9]{7,15}\b"                #It will have max last 15 digits 
match_obj = re.findall(pat, phones)
print(match_obj)

pat = r"\b[0-9]{7,15}\b"               #should not get invalid phone numbers only valid.
match_obj = re.findall(pat, phones)
print(match_obj)

print("-----finditer-----")
# finditer()- matches all returns as iterator using for loop.
pat = r"\b[0-9]{7,15}\b"               
match_obj_iter = re.finditer(pat, phones)
print(match_obj)

for matches in match_obj_iter:
    print(matches)