import random
import numpy as np
import matplotlib.pyplot as plt
from ex2_2 import Point2D

class LinearEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.vertical = (b == 0)

    def gety(self, x):
        if self.vertical:
            raise ValueError("Cannot compute y for vertical line")
        return -(self.a * x + self.c) / self.b

    # methods for ex 2.7
    def evaluate(self, point):
        """Return ax + by + c for a given Point2D."""
        return self.a * point.x + self.b * point.y + self.c

    def positive(self, point):
        """Return True if point is in the positive half-plane."""
        return self.evaluate(point) > 0

    def negative(self, point):
        """Return True if point is in the negative half-plane."""
        return self.evaluate(point) < 0

def line_from_points(p1, p2):
    a = p2.y - p1.y
    b = -(p2.x - p1.x)
    c = -(p1.x * a + p1.y * b)
    return LinearEquation(a, b, c)

#function for ex2.6
def random_line_in_rectangle(p1, p2):

    # Generate two random points in the rectangle
    x1 = random.uniform(min(p1.x, p2.x), max(p1.x, p2.x))
    y1 = random.uniform(min(p1.y, p2.y), max(p1.y, p2.y))
    x2 = random.uniform(min(p1.x, p2.x), max(p1.x, p2.x))
    y2 = random.uniform(min(p1.y, p2.y), max(p1.y, p2.y))

    pt1 = Point2D(x1, y1)
    pt2 = Point2D(x2, y2)

    return line_from_points(pt1, pt2)

# Define the line: 2x - y + 3 = 0
line = LinearEquation(a=2, b=-1, c=3)

x_values = np.linspace(0, 10, 200)
y_values = [line.gety(x) for x in x_values]

# Plot
plt.plot(x_values, y_values, color='blue', linewidth=2, label='2x - y + 3 = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line 2x - y + 3 = 0')
plt.grid(True)
plt.legend()
plt.show()

print(line.gety(6))

p1 = Point2D(1, 2)
p2 = Point2D(4, 6)


line = line_from_points(p1, p2)
print(f"Line coefficients: a={line.a}, b={line.b}, c={line.c}")

print("y at x=2:", line.gety(2))