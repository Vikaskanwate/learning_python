# Write a Python program to find the length of the longest streak of consecutive numbers in a list where even and odd numbers strictly alternate.


# lst = [1,2,3,4,5]
lst=[1,3,5,7,9]
count = 1
maxCount = 1
for i in range(1,len(lst)):
    if (lst[i-1] % 2 == 0 and lst[i] % 2  != 0) or (lst[i-1] % 2 != 0 and lst[i] % 2 == 0):
        count+=1
        maxCount = max(maxCount,count)
    else:
        count = 1

print(maxCount)


