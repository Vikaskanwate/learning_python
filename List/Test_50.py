# find matching work pair
list1 = ["apple", "banana", "cherry", "date", "grape", "kiwi"]
list2 = ["banana", "date", "fig", "grape", "melon", "apple"]

s = set()
for i in list1:
    for j in list2:
        if i == j:
            s.add(i)
print(list(s))

print(list(set(list1) & set(list2)))