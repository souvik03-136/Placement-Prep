# 6. Inheritance
# Child class can use properties/methods of parent class.
# Can also override parent methods.


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):   # method overriding
        print("Woof Woof")

class Cat(Animal):
    pass

d = Dog()
d.speak()

c = Cat()
c.speak()   # Uses parent method