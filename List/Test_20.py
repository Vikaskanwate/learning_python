lst1 = [12,34,4,2,423]
lst2 = [2,25,1,68,58]
lst3 = sorted(lst1 + lst2)
print(lst3)
def s(lst3):
    temp = 0
    for i in range(len(lst3)):
        for j in range(0,len(lst3) - i -1):
            if lst3[j] > lst3[j+1]:
                # temp = lst3[j]
                # lst3[j] = lst3[j+1]
                # lst3[j+1] = temp 
                # new swpping technique special in python
                lst3[j], lst3[j+1] = lst3[j+1], lst3[j]
    return lst3

print(s(lst3))