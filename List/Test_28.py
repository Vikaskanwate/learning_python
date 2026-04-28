# frequency of words
s = 'I love python,python loves me'
st =s.replace(","," ").split()
freq={}
for ch in st:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key,value in freq.items():
    print(key,":",value)

