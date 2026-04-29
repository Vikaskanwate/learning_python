# 1. The Frequency Counter (The "Classic")
# Task: Given a string or a list, count how many times each element appears.

# Sample Input: ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# Expected Output: {'apple': 3, 'banana': 2, 'cherry': 1}

# Key Logic: Iterate through the list. If the item is in the dictionary, increment its value. If not, add it with a value of 1.

lst = ['apple','banana','apple','cherry','banana','apple']
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)