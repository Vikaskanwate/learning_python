# count word by length

lst = ["hi","hello","cat","dog"]

length_dict = {}
for w in lst:
    length = len(w)
    if length in length_dict:
        length_dict[length] +=1
    else:
        length_dict[length] = 1