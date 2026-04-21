# reverse the string
st = "I Love python."
ans = ""

a = "".join(reversed(st))
print(a)

for ch in st:
    ans = ch + ans
print(ans)