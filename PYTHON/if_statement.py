# if = Do some code only IF some condition is True else do something else


age = int(input("Enter your age: "))
if age >= 18 and age <= 100:
    print("you are now signed up to vote!")
elif age > 100:
    print("you are too old to vote!")
elif age < 0:
    print("you are not born yet!")
else:
    print("you must be 18+ to sign up to vote!")
    

