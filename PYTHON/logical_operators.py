# logical operators = evaluate multiple conditions(or, and, not)
#                 or = at least one condition is true
#                and = all conditions must be true
#                not = inverts the results or conditions (not true, not false)
## For logicall oprator "OR"

temp = 20
is_raising = True

if temp > 35 or temp < 0 or is_raising:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is scheduled")
    
    