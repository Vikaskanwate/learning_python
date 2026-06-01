# Question 6: Duplicate Removal with Order Preservation

# You are cleaning a dataset but must preserve order.

# Task:

# Implement a class DuplicateRemover with:
# Input: [1, 2, 2, 3, 1]
# Output: [1, 2, 3]
class DuplicateRemover():
    def __init__(self, data):
        self.data = data
    
    def remove_duplicates(self):
        return list(dict.fromkeys(self.data))


print(DuplicateRemover([1, 2, 2, 3, 1]).remove_duplicates())