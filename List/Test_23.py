# Write a Python program to find the length of the longest streak of strictly increasing consecutive numbers in a list.

lst = [1,2,3,2,3,4,5]

count = 1
countMax = 1
for i in range(1,len(lst)):
    if lst[i] > lst[i-1]:
        count += 1
        countMax = max(countMax,count)
    else:
        count = 1

print(countMax)