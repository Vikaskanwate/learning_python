# Generate a new string such that:

# Characters appear only once
# Order should be based on their first occurrence
# But include only those characters whose frequency is more than 1

# s = "aabccdefffg" input 
# acf output

s = "aabccdefffg"

d = {}
for i in s:
    d[i] = d.get(i,0)+1

result = ""
# for key,value in d.items():
#     if value > 1:
#         result += key

seen = set()

for ch in s:
    if ch not in seen and d[ch] > 1:
        result += ch
        seen.add(ch)

print(result)