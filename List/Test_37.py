# count word by length

lst = ["hi","hello","cat","dog"]

length_dict = {}
for w in lst:
    length = len(w)
    if length not in length_dict:
        length_dict[length] = []

    length_dict[length].append(w)


print(length_dict)