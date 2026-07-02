# Membership Operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tupe, set, or dictionary)
#                       1. in
#                       2. not in
"""
word = "apple"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} letter in the word! ")
else:
    print(f"letter {letter} was not found")
    
"""

"""
students = {"samuel", "muche", "babi"}
student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found ")
else: 
    print(f"{student} is a student")
    
"""
# the last example
email = "samicode@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")
