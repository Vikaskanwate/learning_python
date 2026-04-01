var = "hello World"
var1 = ",Good Morning"
# print first character in capital
print(var.capitalize())
# print String in lowercase
print(var.lower())
# print string in uppercase
print(var.upper())
# first word will be capitalized
print(var.title())
# swap the word if capital it goes lower and vise versa
print(var.swapcase())
# removes leading white space
print(var.strip())
# raplace substring o with a
print(var.replace("o","a"))
# splits string into list
print(var.split(" "))
# to join the string first on what basis to join
print(" ".join([var,var1]))
# return index of substring if not available it will return -1
print(var1.find("e"))
# count the occurence of substring
print(var1.count("a"))
print(var.isalnum())

print(var.isspace())
print(dir(var))
# print(help(var.isspace()))
# it will check if the string is empty or not
# it also get the lowercase stricter 
print(var.casefold())
# if i want to put padding before or after string 
print(var.center(30,"o"))
# to encode converts into bite object
print(var.encode())

print(var.endswith("a"))


