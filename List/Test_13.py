# count frequency of the words in string
s = 'hello'
ans = ''
for i in s:
    cnt = s.count(i)
    if i not in ans:
        ans += f"{i}:{cnt} "

print(ans)