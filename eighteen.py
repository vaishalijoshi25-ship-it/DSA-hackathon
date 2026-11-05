n = int(input("Enter a num:"))
total = 0
i = 1
while i < n:
    if n % i == 0:
        total = total + i
    i = i + 1
if total == n:
    print("True")
else:
    print("False")