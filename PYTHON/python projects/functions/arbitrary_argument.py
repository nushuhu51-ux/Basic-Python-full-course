# *args = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple key
#             * unpacking operator

# ARBITRARY Argument
"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))

"""
"""
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Dr", "samuel", "teshale", "terefe")
"""

"""
def print_address(**kwargs):
    for value in kwargs.values():
      print(value)
print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="AA",
              zip="54321")
              
              """
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get("city")} {kwargs.get('zip')}")
shipping_label("Dr.", "samuel", "Teshale", "III",
               street="123 Fake St.",
              city="Detroit",
              state="AA",
              zip="54321")