str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
count1 = 0
count2 = 0
for ch in str1:
    count1 += 1
for ch in str2:
    count2 += 1
if count1 == count2:
    print("True")
else:
    print("False")