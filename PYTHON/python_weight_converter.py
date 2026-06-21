weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (kg or lb) ")

if unit == "kg":
    weight = weight*2.205
elif unit == "lb":
    weight == weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} is not a valid unit. please use kg or lb ")
    
print(f"your weight is: {weight:.2f} {unit}")