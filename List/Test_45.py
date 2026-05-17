# how to use sorted() function in python


# sort list in descending order
def sort_desc(nums):
    return sorted(nums,reverse=True)
# print(sort_desc([4,1,7,3]))


# Sort Words by Length, Then Alphabetically
# Problem:  
# Given a list of words, sort them first by length, then alphabetically if lengths are equal.

def sort_words(words):
    return sorted(words,key=lambda x : (len(x),x))

# print(sort_words(["pear", "apple", "fig","fat", "banana"]))

# Sort Students by Score, Then Name
# Problem:  
# You are given a list of dictionaries with student names and scores.
# Sort them by score (highest first), and if scores are equal, sort by name alphabetically.

def sort_students(students):
    return sorted(students, key=lambda x:(-x["score"],x['name']))
students = [
     {"name": "Alice", "score": 90},
    {"name": "Aeice", "score": 90},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 90}
]
# print(sort_students(students))


# Write a function that returns a new dictionary where the students are sorted alphabetically by their names (the keys).
std = {
    "Charlie": 85,
    "Alice": 90,
    "Bob": 75
}
def sort_by_keys(std):
    return dict(sorted(std.items()))
# print(sort_by_keys(std))

# Challenge: Sort by Values
# Task:  
# Write a function that returns a new dictionary where the students are sorted by their scores (the values) in ascending order.


marks = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 95,
    "David": 72,
    "Eve": 88,
    "Frank": 65,
    "Grace": 95,
    "Helen": 88
}



def sort_by_marks(marks):
    return dict(sorted(marks.items(),key=lambda x : -x[1]))

# print(sort_by_marks(marks))

# Challenge: Sort by Values (Descending), Then by Keys

# Task:  
# Write a function that returns a new dictionary where:

# Students are sorted by their marks in descending order.

# If two students have the same mark, they should be sorted alphabetically by name.

def sort_by_marks_and_name(marks):
    return dict(sorted(marks.items(),key=lambda x : (-x[1],x[0])))
# print(sort_by_marks_and_name(marks))


# Top N Students with Multi‑Criteria Sorting

# Task:  
# Write a function that:

# Sorts students by marks in descending order.

# If two students have the same mark, sorts them alphabetically by name.

# Returns only the top N students (where N is passed as a parameter).
 
def top_N(marks,N):
    return dict(sorted(marks.items(),key=lambda x : (-x[1],x[0]))[:N])
# print(top_N(marks,3))


stud = {
    "Alice": {"math": 88, "science": 92},
    "Bob": {"math": 95, "science": 85},
    "Charlie": {"math": 72, "science": 90}
}

print(sorted(stud.items(),key= lambda x : x[1]["science"]))
