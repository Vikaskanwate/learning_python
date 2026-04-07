num = 111
rev = 0
temp = num
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if(temp == rev):
    print("number is prime")
else:
    print("Number is not prime")