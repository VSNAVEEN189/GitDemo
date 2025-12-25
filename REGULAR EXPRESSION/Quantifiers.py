# Quantifiers are symbols or characters to tell how match quantity 

# + matches one or more repititions of the previous pattern 
# * zero or more
# ? zero or  one
# {n} n numbers of quantifiers


# Using metacharacters with quantifiers to get exact number
import re
message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."

print("----{n} number of quantifiers----")
pat = r"[a-z]{4}"                       #The first occurence all the four smallcase character.
match_obj = re.search(pat, message)
print(match_obj)

pat = r"[A-Z][a-z]{5}"                  # One uppercase followed by 5-small letters. It will apply on preceding [a-z].   
match_obj = re.search(pat, message)
print(match_obj)

pat = r"[A-Z][a-z]{2,5}"                # Minimum 2 or 5 small character. 
match_obj = re.search(pat, message)
print(match_obj)

print("-----(+) matches one or more repititions of the previous pattern------")
# + 
pat = r"[A-Z][a-z]+"                    # matches one or more repititions of the previous pattern. 
match_obj = re.search(pat, message)
print(match_obj)

print("----(?) zero or one-----")
# ? 0 or 1 repititions of the previous pattern 
pat = r"[A-Z][a-z]?"                     # Either zero or one should match, If not also okay .
match_obj = re.search(pat, message)
print(match_obj)

print("----(*) zero or more-----")
# * 0 or more repititions of the previous pattern 
pat = r"[A-Z][a-z]*"                     # If small letters is not present after uppercase letter it's okay
match_obj = re.search(pat, message)
print(match_obj)