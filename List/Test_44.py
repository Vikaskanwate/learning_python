# Split this into chunks such that:

# Each chunk contains unique characters only
# When a duplicate is encountered, start a new chunk

s = "pythonprogramming"
result = []
current = ""
seen = set()
for ch in s:
    if ch in seen:
        result.append(current)
        current = ch
        seen = {ch}
    else:
        current += ch
        seen.add(ch)
        
if current:
    result.append(current)

print(result)

