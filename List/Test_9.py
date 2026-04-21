# sum of digits of numbers
n = int(input('Enter the number\n'))
s = 0
while n > 0:
    s += n % 10
    n //= 10

print(s)