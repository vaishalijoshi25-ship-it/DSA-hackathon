N = int(input("Enter a decimal number: "))
binary = ""
while N > 0:
    remainder = N % 2
    binary = str(remainder) + binary
    N = N // 2
print(binary)