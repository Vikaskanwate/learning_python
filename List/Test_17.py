# find largest and smallest element in list
lst = [4,5,8,1,3]
minNum= min(lst)
maxNum = max(lst)
print("Minimum num " ,minNum, "maximum num ",maxNum)
minN = float('inf')
maxN = float('-inf')
for i in lst:
    if i > maxN:
        maxN = i
    if i < minN:
        minN = i

print(minN , " " , maxN)