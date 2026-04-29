# Task: Create a new dictionary where the keys become values and values become keys.

# Input: {'name': 'Vikas', 'role': 'Developer'}

# Goal: {'Vikas': 'name', 'Developer': 'role'}

d =  {'name': 'Vikas', 'role': 'Developer'}
d1 = {}
for key , value in d.items():
    d1[value] = key

print(d1)