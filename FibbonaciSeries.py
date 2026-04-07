num = 10
f = 0
s = 1
num -= 2
print(f,s,end=" ")
while num > 0:
    third = f + s
    f = s
    s = third
    print(third ,end=" ")
    num-=1