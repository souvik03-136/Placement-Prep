# 3. Instance vs Class Attributes
# # Explanation:
# # Instance attribute → unique per object
# # Class attribute → same for all objects

class Dog:
    species = "Mammal"   # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

d1 = Dog("Buddy")
d2 = Dog("Charlie")

print(d1.name, d1.species)
print(d2.name, d2.species)