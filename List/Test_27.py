# Problem:  
# Write a Python program that takes a sentence and performs the following using only string concepts:

# Remove leading/trailing spaces.

# Convert the sentence to lowercase.

# Split into words.

# Count how many words are palindromes.

# Find the most frequent word (case‑insensitive).

# Print the longest palindrome word (if any).

# Input: " Madam Arora teaches malayalam "

# Palindrome count: 3 (Madam, Arora, malayalam)

# Most frequent word: "madam" (appears once, but tie → first)

# Longest palindrome: "malayalam"

def isPalindrome(str):
    if str == str[::-1]:
        return True
    return False

# s = " Madam Arora teaches malayalam "
s = " Level level civic Civic rotor "

lst = s.lower().strip().split(" ")
count= 0
for ch in lst:
    if isPalindrome(ch):
        count += 1
    else:
        None

mostFreqWord = ""
maxCount = 0
for w in lst:
    c = lst.count(w)
    if c > maxCount:
        maxCount = c
        mostFreqWord = w


longest = ""
for ch in lst:
    if len(ch) > len(longest) and isPalindrome(ch): longest = ch


print("Palindrome count:",count)
print("Longest palindrome:",longest)
print("Most frequent word:",mostFreqWord)


