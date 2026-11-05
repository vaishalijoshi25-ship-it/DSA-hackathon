text = input("Enter a string: ")
upper = 0
lower = 0
digits = 0
special = 0
for ch in text:
    if ch >= 'A' and ch <= 'Z':
        upper += 1
    elif ch >= 'a' and ch <= 'z':
        lower += 1
    elif ch >= '0' and ch <= '9':
        digits += 1
    else:
        special += 1
print("Upper:", upper)
print("Lower:", lower)
print("Digits:", digits)
print("Special:", special)