# Question 5: Pattern-Based Word Filter

# You are building a search system.

# Task:

# Implement a class WordMatcher with:

# __init__(self, words)
# match(self, pattern):
# pattern like "a*e" → starts with a, ends with e

# Input: ["apple", "axe", "age"], pattern="a*e"
# Output: ["apple", "axe", "age"]

class WordMatcher():
    def __init__(self,words):
        self.words = words
    def match(self,pattern):
        # ans = []
        # for w in self.words: 
        #     if w[:1] == pattern[:1] and w[-1:] == pattern[-1:]:
        #         ans.append(w)
        # return ans
        ans = []

        parts = pattern.split("*")

        start = parts[0]
        end = parts[-1]

        for w in self.words:
            if start and not w.startswith(start):
                continue
            if end and not w.endswith(end):
                continue
            ans.append(w)
            
        return ans
print(WordMatcher(["apple", "axe", "age"]).match("a*e"))