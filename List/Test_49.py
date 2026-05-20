# remove duplicate element
list1 = [1, 2, 3, 4, 5, 2, 3]
list2 = [3, 4, 4, 3]

s = list(set(list1))
print(s)

if all(i in list1 for i in list2):
    print("list2 is subset of list1")
else:
    print("list2 is not subset of list1")