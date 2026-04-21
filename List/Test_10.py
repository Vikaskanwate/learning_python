n = int(input('Enter the number\n'))

def fib(n):
    lst = [0,1]
    first,sec = 0,1
    for i in range(2,n):
        third = first + sec
        first = sec
        sec = third
        lst.append(third)
    return lst

print(fib(n))