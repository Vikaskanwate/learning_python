#invert a dictionary swap key's with values
students = {
    "Alice": 85,
    "Charlie": 78,
    "Bob": 92,
    "Eva": 95,
    "David": 90
}

d = {}
for key,value in students.items():
    d[value] = key

print(d)

sorted_student = dict(sorted(students.items()))
print(sorted_student)