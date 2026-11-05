n = int(input("Enter a num:"))
num = 2
while num <= n:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i = i + 1
    if count == 2:
        print(num, end=" ")
    num = num + 1