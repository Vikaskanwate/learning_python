# word = "madam"
# if word == word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

word = "madam"

name = "".join(reversed(word))

if word == name:
    print()
    print("palindrome")
else:
    print("not palindrome")