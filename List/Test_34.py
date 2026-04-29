# group even and odd
input = [1,2,3,4,5]
d = {}
lst = []
lst1 = []
for i in input:
    if i % 2 == 0:
        lst.append(i)
        d["even"]  = lst
    else:
        lst1.append(i)
        d["odd"] = [lst1]
    
print(d)