# 11. Property Decorators (Getters & Setters)
# Use @property for getter and @name.setter for setter.
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):   # getter
        return self._name

    @name.setter
    def name(self, value):  # setter
        if len(value) < 3:
            raise ValueError("Name too short!")
        self._name = value

p = Person("Raj")
print(p.name)
p.name = "Souvik"
print(p.name)