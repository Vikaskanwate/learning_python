# Problem 1: Non-Repeating Substring Length
# Write a Python function that returns the length of the longest substring without repeating characters.

# Example Test Cases

# Input: "abcabcbb" → Output: 3 (substring "abc")

# Input: "bbbbb" → Output: 1 (substring "b")

# Input: "pwwkew" → Output: 3 (substring "wke")

# Input: "" → Output: 0
s = "pwwkew"
def RSub(s):
    seen = set()
    left = 0
    maxLen = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            # remove from left side until duplicate is gone
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxLen = max(maxLen, right - left + 1)
    
    return maxLen


print(RSub(s))