# keyword arguments = an argument preceded by an identifier helps with readability
#                     oreder of an argument doen't matter

### 2. keyword argument
"""
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello", title = "Mr.", first = "samuel", last="teshale", )

"""
"""
for x in range(1, 11):
    print(x, end=" ")
    
    """
    # another example
    
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=2, area=251, first=92539, last=6586)
print(phone_num)