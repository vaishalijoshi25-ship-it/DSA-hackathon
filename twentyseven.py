text = input("Enter a string: ")
result = ""
for ch in text:
    if ch >= 'A' and ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch
print("Lowercase:", result)