# count the number of charcters 
# if character is repeated do not count

word = "programming"
# result = ""
# for char in word:
#     if char not in result:
#         result += char
# print(len(result))
print(len(set(word)))