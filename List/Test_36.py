#invert a dictionary swap key's with values
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 95
}

d = {}
for key,value in students.items():
    d[value] = key

print(d)