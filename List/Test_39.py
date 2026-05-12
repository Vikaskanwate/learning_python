# Combo Challenge (Dictionary + Map + Filter + Reduce)
# Problem:  
# Given a list of words,

# Filter out words shorter than 4 letters.

# Map them to uppercase.

# Count frequency of each word.

# Reduce to find the longest word.

from functools import reduce

words = ["apple", "bat", "car", "banana", "dog", "elephant"]

filerted_words = list(filter(lambda w : len(w) >= 4,words))

words = list(map(lambda word:word.upper(),words))

freq = {}
for w in words:
    freq[w]= freq.get(w,0)+1

largestWord = reduce(lambda a,b:a if len(a) > len(b) else b ,words)

print(words)
print(words)
print(freq)
print(largestWord)