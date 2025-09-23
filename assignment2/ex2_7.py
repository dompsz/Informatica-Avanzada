import matplotlib.pyplot as plt
import numpy as np
import random
from ex2_2 import Point2D, random_points_in_rectangle
from ex2_4_and_5 import LinearEquation

line = LinearEquation(a=2, b=-1, c=3)

# Plot line for x in [0,10]
x_values = np.linspace(0, 10, 200)
y_values = [line.gety(x) for x in x_values]

plt.plot(x_values, y_values, color='black', linewidth=2, label='2x - y + 3 = 0')

rect_p1 = Point2D(0, 3)
rect_p2 = Point2D(10, 23)
points = list(random_points_in_rectangle(rect_p1, rect_p2, 100))

x_pos, y_pos = [], []
x_neg, y_neg = [], []

for p in points:
    if line.evaluate(p) > 0:   # points above line
        x_neg.append(p.x)
        y_neg.append(p.y)
    elif line.evaluate(p) < 0: # points below line
        x_pos.append(p.x)
        y_pos.append(p.y)

plt.scatter(x_pos, y_pos, color='green', alpha=0.6, label='Positive half-plane')
plt.scatter(x_neg, y_neg, color='red', alpha=0.6, label='Negative half-plane')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Points Colored by Half-Plane')
plt.legend()
plt.grid(True)
plt.show()
