# count vowels and cons in string
st = "mississippi"
cntv = 0
cntc = 0
for i in st:
    if i in "aeiou":
        cntv+=1
    else:
        cntc+=1

print("vowels:",cntv)
print("consonants:",cntc)