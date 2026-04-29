# find the maximum in dict

marks = {'Maths': 95, 'Physics': 88, 'Chemistry': 92, 'English': 98}

maxSubject = None
maxMarks = -1

for subject , marks in marks.items():
    if marks > maxMarks:
        maxMarks = marks
        maxSubject = subject

print(f"Maximum marks is in subject {maxSubject} ans marks are :{maxMarks}")