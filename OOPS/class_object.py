# 1. Class & Object
# Explanation:
# A class is a blueprint (like a design).
# An object is the actual thing created from the class.
# File Name: class_object.py

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Object creation
c1 = Car("Tesla", "Model S")
c1.drive()
