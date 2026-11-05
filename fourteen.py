a = int(input("Enter a num:"))
b = int(input("Enter a num:"))
x = a
y = b
while b != 0:
    remainder = a % b
    a = b
    b = remainder
gcd = a
lcm = (x * y) // gcd
print(lcm)