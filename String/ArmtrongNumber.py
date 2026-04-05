num = "9475"
n = len(num)
number = int(num)
temp = number
sum = 0

while (number > 0):
    digit = number % 10
    sum += (digit ** n)
    number //= 10

if sum == temp:
    print("number is armstrong")
else:
    print("number is not armstrong")