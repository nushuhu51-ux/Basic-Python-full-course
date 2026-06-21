# conditional expression = A one line shortcutfor the if-else statement (ternary operator)
#                       print or assign one of two values based on a condition
#                       X if condition else Y

num = 5
a = 6
b = 7
age = 23
temperature = 30
user_role = "gust"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
status = "Adult" if age >= 18 else "child"
print(status)
weather = "HOT" if temperature > 20 else "COLD"
print(weather)
access_level = "Full access" if user_role == "admin" else "Limited Access"
print(access_level)