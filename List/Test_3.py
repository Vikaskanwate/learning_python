st = "Hello World!"

lst = st.split(" ")
rev = []
for i in lst:
    rev.append(i[::-1])
    
print(rev)

joined = " ".join(rev) 
print(joined)