# Construct a result such that:

# Keep only elements appearing exactly once
# Maintain original order

data = [12, "hello", 15, "world", 12, "hello", 18, "code"]

d = {}
for i in data:
    d[i] = d.get(i,0)+1

result = []
seen = set()
for i in data:
    if i not in seen and d[i] == 1:
        result.append(i)
print(result)