#find the student with highest marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 95
}
# print(max(students))

maxMarks = -1
st = None
for student , marks in students.items():
    if marks > maxMarks:
        maxMarks = marks
        st = student
print(f"student with highest marks : {st} and Marks : {maxMarks}")
