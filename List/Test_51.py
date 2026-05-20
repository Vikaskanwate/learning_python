# count char frequency
str = "banana"
lst = []
for i in str:
    cnt = str.count(i)
    if i not in lst:
        lst.append(i)
        print(f"{i} : {cnt}")