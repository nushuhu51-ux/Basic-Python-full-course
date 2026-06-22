# format specifiers = {:flags}
# format a value based on what flags are inserted

# :. (number)f = round to that many decimal places (fixed point)
# Example: f"{12.345:.2f}" → 12.35

# :(number) = allocate that many spaces
# Example: f"{'Hi':10}" → Hi + spaces

# :03 = allocate and zero pad that many spaces
# Example: f"{7:03}" → 007

# :< = left justify
# Example: f"{'Hi':<10}" → Hi        

# :> = right justify
# Example: f"{'Hi':>10}" →         Hi

# :^ = center align
# Example: f"{'Hi':^10}" →     Hi    

# :+ = use a plus sign to indicate positive value
# Example: f"{5:+}" → +5

# := = place sign to leftmost position
# Example: f"{-1234:=+10}"

# :  = insert a space before positive numbers
# Example: f"{5: }" → " 5"

# :, = comma separator
# Example: f"{1000000:,}" → 1,000,000



price1 = 3.14159
price2 = -98.65
price3 = 12.34

print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")