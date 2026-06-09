# 3. Sort Strings by Last Character
# Given a list of strings, sort them by their last character. If last characters match, sort alphabetically.

words = ["apple", "banana", "pear", "grape"]
# Expected: ['banana','pear','apple','grape']
nums = [3,None,1,None,2]
# Expected: [1,2,3,None,None]
print(sorted(nums, key= lambda x : ( x is None,x)))
res = sorted(words, key= lambda x : x[-1])
print(res)