# Build a multiplication table for numbers 1 through 10
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
