# Sort by Frequency, Then Value
# Given a list of integers, sort them by frequency (ascending). If two numbers have the same frequency, sort them by value (descending).
# Expected: [1,4,4,2,2,3,3,3]

from collections import Counter
nums = [4,4,1,2,2,3,3,3]
freq = dict(Counter(nums))
print(dict(freq))

# print(sorted(freq.items(),key=lambda x : x[1]))
print(sorted(nums,key=lambda x : (freq[x],-x)))




