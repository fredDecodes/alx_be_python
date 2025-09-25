# Draw a pattern using a while loop for rows and a for loop for asterisks
pattern_size = int(input("Enter the size of the pattern: "))
row = 0
while row < pattern_size:
    for i in range(pattern_size):
        print("*", end=" ")
    print()  # Move to the next line after each row
    row += 1