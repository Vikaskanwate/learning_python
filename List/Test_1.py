# lst = [10,45,4,20,99]
lst = [12,12,10,8]
largest = 0
second_largest = 0
for i in lst:
    if i > largest :
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
        

print(second_largest)

