class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(2,5)
p2 = Point(89,57)
p3 = Point(56,78)

print(p1)
print(p2)
print(p3)