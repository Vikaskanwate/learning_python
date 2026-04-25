# Write a Python program that takes a sentence and performs the following transformations using only string concepts:

# Remove leading/trailing spaces.

# Convert the sentence to lowercase.

# Capitalize the first letter of each word.

# Remove duplicate words (case‑insensitive).

# Count the number of vowels and consonants in the final cleaned sentence.

# Find the longest word in the sentence.
s = " Java is IS fun FUN "
words = s.lower().strip().split(" ")
ans = ""
for i in range(len(words)):
    words[i]= words[i].capitalize()


for ch in words:
    if ch not in ans:
        ans += ch +" "
ans = ans.strip(" ")


countVowels = 0
countCons = 0
for ch in ans.split(" "):
    for i in ch:
        if i in "aeiouAEIOU":
            countVowels+=1
        else:
            countCons+=1


longest = ""
for ch in ans.split(" "):
    if len(ch) > len(longest): longest = ch


print("Cleaned sentence:",ans)
print("Vowels:",countVowels , "\nConsonants:" ,countCons)
print("Longest word:",longest)
