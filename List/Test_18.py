# removing duplicate from list preserv the order
# lst = [1, 2, 2, 3, 4, 4, 4, 5]
lst = ["apple", "banana", "apple", "cherry", "banana", "date"]
ans = []
for i in lst:
    if i not in ans:
        ans.append(i)
print(ans)