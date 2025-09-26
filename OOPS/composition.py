# 10. Composition (HAS-A relationship)
# One class contains object of another class.
# File Name: composition.py

class Engine:
    def start(self): print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

car = Car()
car.drive()
