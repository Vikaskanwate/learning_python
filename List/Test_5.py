# longest word in string
st = "Programming is fun"
lst = st.split(" ")
max = 0
# print(max(lst))
for i in lst:
    a = len(i)
    if a > max:
        max = a

for j in lst:
    if len(j) == max:
        print(j)
        break
    
