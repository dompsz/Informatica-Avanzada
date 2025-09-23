import matplotlib.pyplot as plt
import numpy as np
from ex2_2 import Point2D
from ex2_4_and_5 import random_line_in_rectangle

# Rectangle vertices
p1 = Point2D(-1, -1)
p2 = Point2D(1, 1)

# x values for plotting
x_values = np.linspace(p1.x - 0.5, p2.x + 0.5, 200)

plt.figure(figsize=(6,6))

# Generate and plot random lines
for _ in range(20):
    line = random_line_in_rectangle(p1, p2)
    # ignore vertical lines
    if not line.vertical:
        y_values = [line.gety(x) for x in x_values]
        plt.plot(x_values, y_values)
    else:
        x_vert = -line.c / line.a
        plt.axvline(x=x_vert)

# Draw rectangle boundary
plt.plot([p1.x, p2.x, p2.x, p1.x, p1.x],
         [p1.y, p1.y, p2.y, p2.y, p1.y], color='black', linewidth=1.5, label='Rectangle')

plt.xlim(p1.x - 0.5, p2.x + 0.5)
plt.ylim(p1.y - 0.5, p2.y + 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('5 Random Lines Crossing the Rectangle')
plt.grid(True)
plt.show()
