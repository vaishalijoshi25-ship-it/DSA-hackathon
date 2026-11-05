n = int(input("Enter a num:"))
original = n
temp = n
digits = 0
total = 0
while temp > 0:
    digits = digits + 1
    temp = temp // 10
temp = n
while temp > 0:
    digit = temp % 10
    power = 1
    i = 1
    while i <= digits:
        power = power * digit
        i = i + 1
    total = total + power
    temp = temp // 10
if total == original:
    print("True")
else:
    print("False")