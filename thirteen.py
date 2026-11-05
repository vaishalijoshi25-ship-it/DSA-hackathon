a = int(input("Enter a num:"))
b = int(input("Enter a num:"))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(a)