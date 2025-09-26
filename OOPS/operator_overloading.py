# 8. Operator Overloading
# Explanation:
# We can redefine operators (+, -, *, etc.) for custom classes.

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):   # Overload +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):   # String representation
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)   # (6, 8)