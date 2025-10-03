#5

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter term number: "))

print(x,y,end=" ")

for i in range(z-2):
    a = x+y
    x=y
    y=a
    print(a, end=" ")
