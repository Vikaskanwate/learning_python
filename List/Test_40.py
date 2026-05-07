
d = {}
def freq(cart):
    for item in cart:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

result  = freq(["apple", "banana", "apple", "orange", "banana", "apple"])

print(result)