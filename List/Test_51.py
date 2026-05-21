# count char frequency
st = "banana"
lst = []
for i in st:
    cnt = st.count(i)
    if i not in lst:
        lst.append(i)
        print(f"{i} : {cnt}")