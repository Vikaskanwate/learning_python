# used dictionary 
freq={}

for ch in "hello":
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key, value in freq.items():
    print(key, ":", value)

