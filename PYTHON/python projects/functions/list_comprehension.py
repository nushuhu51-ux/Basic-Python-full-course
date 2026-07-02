# List comprehesion = A concise way to create lists in python
#                    compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]
"""
doubles = [ x*2 for x in range(1, 11)]
triples = [ x*3 for x in range(1, 11)]
squares = [ x*x for x in range(1, 11)]

print(doubles, triples, squares)
"""
"""
# for strings 

fruits = ["apples", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

"""

# for numbers or integers
numbers = [1, -2, 3, -4, 5, -6]
posetive_nums = [num for num in numbers if num > 0 ]
negative_nums = [num for num in numbers if num < 0 ]
print(posetive_nums, negative_nums)