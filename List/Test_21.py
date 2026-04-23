# Write a Python program to find the longest streak of consecutive 1s in a binary list.
# lst = [1,1,0,1,1,1,0,1]
lst =[0,0,0]
count = 0
maxCount = 0

for i in lst:
    if i == 1:
        count+=1
        if count > maxCount:
            maxCount = count
    else:
        count = 0

print(maxCount)
