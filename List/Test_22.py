# Write a Python program to find the longest streak of consecutive vowels (a, e, i, o, u) in a given string.

s = "beautiful"
current= ""
longest = ""
count = 0
maxCount = 0
for ch in s:
    if ch in "aeiou":
        count += 1
        current += ch
        if count > maxCount:
            maxCount = count
            longest = current
    else:
        current = ""
        count = 0

print(maxCount,"(",longest,")")