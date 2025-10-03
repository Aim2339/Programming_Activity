#4

x = int(input("Enter a number: "))
a = 1

for i in range(1, x+1):
    a *= i
print("Factorial of", x, "is", a)