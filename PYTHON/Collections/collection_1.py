# collections = single "variable" used to store multiple values
#   list      = [] ordered and changeable. Duplicate oK
#   set       = {} unordered and immutable, but Add/remove OK. No duplicates
#   Tuple     = () ordered and unchangable. Duplicate ok, Faster

### Lists

fruits = ["apple", "orange", "banana", "coconut"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#print(fruits[:3])
#for fruit in fruits:
#    print(fruit)
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.reverse()
#fruits.clear()
#print(fruits.index("apple"))
#print(fruits.count("banana"))
#print(fruits)

#### Sets

fruits = { "apple", "orange", "banana", "coconut", "coconut"}
#print(dir(fruits))
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()

#### Tuoles
fruits = ( "apple", "orange", "banana", "coconut", "coconut")
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print(fruits.index("apple"))
for fruit in fruits:
    
    print(fruits)