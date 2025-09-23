import random

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    # Generator function for ex2.3
def random_points_in_rectangle(p1, p2, n):
    min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
    min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)

    for _ in range(n):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        yield Point2D(x, y)

p1 = Point2D(2, 3)
p2 = Point2D(2, 3)
p3 = Point2D(4, 5)

print(p1)
print(p3)

print(p1 == p2)
print(p1 is p2)
print(p1 == p3)

p3.x = 2
p3.y = 3
print(p1 == p3)
