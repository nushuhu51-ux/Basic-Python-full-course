# dictionary = a collection of (key:value) pairs
#             ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("Japan"))
"""
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
"""
#capitals.update({"Germany": "Berlin"})
#print(capitals)   
#capitals.pop("China")
#print(capitals)
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
