# return = statement used to end a function
#         and send a result back to the caller
"""
def add(x, y):
    z = x+y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x*y
    return z
def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(6, 4))
print(multiply(6, 5))
print(divide(50, 10))

"""
def create_name(firs, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("sami", "code")

print(full_name)