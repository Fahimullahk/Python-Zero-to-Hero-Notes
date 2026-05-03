class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return (f"{self.x}, {self.y}")

a = Point(2, 3)
print(a)
b = Point(4, 5)
print(b)
print(a + b)

