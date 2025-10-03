#3

x = int(input("Enter a number: "))
total = 0

for i in range(1, x+1):
    total += i
print("Sum of the numbers till", x, "is", total)