# 4. Methods (Instance, Class, Static)
# Instance Method → works with object (uses self)
# Class Method → works with class (uses cls)
# Static Method → general utility, no self or cls

class MathUtils:
    def square(self, x):       # instance method
        return x * x

    @classmethod
    def cube(cls, x):          # class method
        return x ** 3

    @staticmethod
    def add(a, b):             # static method
        return a + b

obj = MathUtils()
print(obj.square(4))
print(MathUtils.cube(3))
print(MathUtils.add(5, 7))