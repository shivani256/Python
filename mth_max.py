n = int(input("Enter the size of the list: "))
arr = []
for i in range(n):
    ele = int(input("Enter element {}: ".format(i+1)))
    arr.append(ele)

m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))

arr.sort()
max1 = arr[-m]
min2 = arr[n - 1]

sum_diff = max1+min2
diff = max1 - min2

print("Mth maximum number:", max1)
print("Nth minimum number:", min2)
print("Sum:", sum_diff)
print("Difference:", diff)
