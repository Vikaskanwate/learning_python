# replace vowels with * 
st = "I love python programming"
ans = ""
for ch in st:
    if ch  in "aeiouAEIOU":
        ans += "*"
    else:
        ans += ch

print(ans)