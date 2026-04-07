num = 153
count = 0
temp = num 
while num != 0:
    num //=10
    count += 1

sum  = 0
Original = temp
while temp != 0:
    digit = temp % 10
    sum += (digit ** count)
    temp //= 10

if(sum == Original):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")