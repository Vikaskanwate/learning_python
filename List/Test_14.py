# find longest word in string
s =  "I love python"
lst = s.split(" ")

ans = ""
max_len = 0
# for i in range(len(lst)):
#     l = len(lst[i])
#     if l >= max:
#         max = l
#         ans =""
#         ans+= lst[i]
# print(ans)

for word in lst:
    if len(word) > max_len:
        max_len = len(word)
        ans = word

print(ans)