import re
s1 = "Python is a programming language"

pat = r"[a-z]{8}"                  
match_obj = re.search(pat, s1)
print(match_obj)

# ^ caret - matches at the beginning of the string only.checks wheather the string starts with some given pattern or not.
print("----(^) Caret----")
pat = r"^[a-z]{8}"                  # Is there all small characters at the beginning of the string.
match_obj = re.search(pat, s1)
print(match_obj)

print("----($) Dollar----")
# $ - matches at the end of the string
pat = r"[a-z]{8}$"                   # Is there small-case characters at the end of a string.
match_obj = re.search(pat, s1)
print(match_obj)

print("-----group() and or(|)------")
#  group- () + | or
email = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com|edu)"                      # Round brackets will take full characters
match_obj = re.search(pat, email)
print(match_obj)