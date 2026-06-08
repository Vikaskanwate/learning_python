class Person:
    __slots__ = ["name","age"]
    def __init__(self,name,age):
        self.name = name
        self.age = age

Person().grade = 0



print(Person("vikas",23).grade)