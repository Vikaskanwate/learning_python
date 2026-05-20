# count maching char in two string

string1 = "hello world"
string2 = "yellow bird"

lst = list(string2)
cnt = 0
for ch in string1:
    if ch in lst:
        cnt += 1
        lst.remove(ch)
print(cnt)