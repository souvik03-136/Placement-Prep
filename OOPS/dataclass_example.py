# 12. Dataclasses
# Quick way to create classes without writing boilerplate code.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: str

s = Student("Alice", 20, "A")
print(s)