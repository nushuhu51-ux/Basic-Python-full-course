# logical operators = evaluate multiple conditions(or, and, not)
#                 or = at least one condition is true
#                and = all conditions must be true
#                not = inverts the results or conditions (not true, not false)
## For logicall oprator "AND"

temp = 10
is_sunny = False

if temp >= 35 and is_sunny:
    print("It's Hot outside🔥")
    print("and It is sunny☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside ❄️")
    print("But, It is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🌤️")
    print("and it is sunny ☀️")
elif temp >= 35 and not is_sunny:
    print("It's Hot outside🔥")
    print("and It is cloudy ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside ❄️")
    print("But, It is cloudy ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🌤️")
    print("and it is cloudy  ☁️")