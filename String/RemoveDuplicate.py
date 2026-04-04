# text = "programming"
# result = ""

# for char in text:
#     if char not in result:
#         result += char
# print(result)

s = "pogramming"
result = "".join(dict.fromkeys(s))
print(result)