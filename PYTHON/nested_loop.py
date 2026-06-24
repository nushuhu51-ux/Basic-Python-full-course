# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                  inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):  # outer loop
    for y in range(columns): # inner loop
        print(symbol, end="")
    print()