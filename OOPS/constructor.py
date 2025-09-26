# 2. Constructor (__init__)
# Explanation:
# Special method in Python classes.
# Runs automatically when an object is created.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 21)
print(s1.name, s1.age)