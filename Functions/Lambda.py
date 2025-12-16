# # Lambda - function is a small,
# #  anonymous function defined using the lambda keyword.

# # syntax
# # lambda arguments: expression

# fun = lambda a, b: a + b
# result = fun(2, 3)
# print(result)  # Output: 5

print("----- Filter and Map using Lambda -----")
# Filter - filter(function, sequence)
# can filter elements from an iterable using the built-in filter() function,
#  a list comprehension, or a standard for loop with an if statement. 
#  typically be converted to a list or other sequence to view the results. 

seq = [1, 2, 3, 4]
odd = filter(lambda x: True if x % 2 != 0 else False, seq)
print(odd)
print(f"Odd numbers in the above sequence are: {list(odd)}")


print("----- Map using Lambda -----")
# Map - map(function, sequence)
# can apply a function to all the items in an iterable using the built-in map() function,

seq = [1, 2, 3, 4]
odd = map(lambda x: x **2, seq)
print(odd)
print(f"Map output: {list(odd)}")