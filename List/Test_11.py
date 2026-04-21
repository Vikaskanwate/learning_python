# factorial of number using recursion
n = int(input('Enter the number\n'))

def factorial(n):
    if n == 0: return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n))