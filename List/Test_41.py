# Given a list of numbers, return only those numbers whose digits sum to an even number, sorted in ascending order.

lst = [23, 44, 15, 81, 30]
ans =[]
rev = 0
for i in lst:
    s = 0
    while i != 0:
        digit = (i % 10)
        s += digit
        i //=10
    if s % 2 == 0:
        print(i)
        ans.append(i) 

print(ans) 
    
    