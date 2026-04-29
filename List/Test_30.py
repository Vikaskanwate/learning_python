# 2. Grouping Data (The "Categorizer")
# Task: Given a list of names, group them by their starting letter.

# Sample Input: ['Alice', 'Bob', 'Charlie', 'Alex']

# Expected Output: {'A': ['Alice', 'Alex'], 'B': ['Bob'], 'C': ['Charlie']}

# Key Logic: Use the first character as the key. If the key exists, .append() the name to the list value. If not, initialize it with a new list: [name].

lst = ['Alice', 'Bob', 'Charlie', 'Alex']

d = {}
for i in lst:
    s = i[:1]
    if s not in d:
        d[s] = [i]
    else:
        d[s].append(i)

print(d)