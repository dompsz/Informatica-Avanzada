import matplotlib.pyplot as plt
from ex2_2 import Point2D, random_points_in_rectangle

p1 = Point2D(1, 2)
p2 = Point2D(5, 6)

n_points = 750

points = list(random_points_in_rectangle(p1, p2, n_points))

x_coords = [p.x for p in points]
y_coords = [p.y for p in points]

plt.scatter(x_coords, y_coords, color='blue', alpha=0.6)

# Zoom out to see the effect
padding_x = (p2.x - p1.x) * 0.5
padding_y = (p2.y - p1.y) * 0.5

plt.xlim(min(p1.x, p2.x) - padding_x, max(p1.x, p2.x) + padding_x)
plt.ylim(min(p1.y, p2.y) - padding_y, max(p1.y, p2.y) + padding_y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'{n_points} Random Points in Rectangle')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # keep square aspect
plt.show()