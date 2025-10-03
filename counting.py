# 2

x = str(input("Enter text: "))
y = x.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in y:
    if i in vowels:
        count += 1
print(count)