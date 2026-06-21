# Typcasting is the process of converting a variable from one data type to another.
# str(), int(), float(), bool()

name = "samuel"
age =25
gpa = 3.2
is_student =True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
age = str(age)

print(type(age))
print(type(gpa))

age += "1"
print(f"your age is {age} years old")

