text = input("Enter a string: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("Palindrome: True")
else:
    print("Palindrome: False")