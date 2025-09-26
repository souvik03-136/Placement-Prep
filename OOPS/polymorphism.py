# 7. Polymorphism
#
# Explanation:
#
# Same method name, different behavior in different classes.
#
# File Name: polymorphism.py

class Bird:
    def fly(self): print("Bird is flying")

class Airplane:
    def fly(self): print("Airplane is flying")

for obj in [Bird(), Airplane()]:
    obj.fly()