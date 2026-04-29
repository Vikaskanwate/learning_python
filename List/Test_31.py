# Task: You have two dictionaries representing sales from two different days. Merge them, but if a product exists in both, sum their values.

# Input 1: {'pen': 5, 'book': 2}

# Input 2: {'pen': 3, 'eraser': 1}

# Expected Output: {'pen': 8, 'book': 2, 'eraser': 1}

d1= {'pen': 5, 'book': 2}
d2 = {'pen': 3, 'eraser': 1}

result = d1.copy()
for key , value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)