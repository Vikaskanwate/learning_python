n = int(input('Enter the number\n'))
def Arm(n):
    l = len(str(n))
    s = 0
    temp = n
    while temp > 0:
        s += ((temp % 10) ** l)
        temp //= 10
    return s

if Arm(n) == n:
    print(n,"Is armstrong number")
else: 
    print(n,"Is not a armstring number")