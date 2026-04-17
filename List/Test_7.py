# lst = [10, 20, 4, 45, 99]
# lst = [8,8,8,8]
lst = [ -5, -2, -9, -1 ]

    
largest = max(lst)
secLargest = float('-inf')
if len(lst) == 0:
    print("EMPTY LIST")
else:
    unique = list(set(lst))   # remove duplicates
    if len(unique) < 2:
        print("No second largest (all elements equal)") 
    else:
        for i in lst:  
            if i > secLargest and i != largest:
                secLargest = i
        print("Second Largest Number : ",secLargest)        