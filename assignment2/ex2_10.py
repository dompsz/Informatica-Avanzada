import numpy as np
import matplotlib.pyplot as plt
from ex2_2 import Point2D
from ex2_4_and_5 import random_line_in_rectangle
from ex2_9 import is_linearly_separable

def find_separator(set1, set2, max_attempts=10000):
    # Compute bounding rectangle that covers both sets
    xs = [p.x for p in set1 + set2]
    ys = [p.y for p in set1 + set2]
    p1 = Point2D(min(xs), min(ys))
    p2 = Point2D(max(xs), max(ys))

    for _ in range(max_attempts):
        line = random_line_in_rectangle(p1, p2)
        if is_linearly_separable(line, set1, set2):
            return line
    return None

iris = np.loadtxt("../training.txt")

setosa = [Point2D(x[2], x[3]) for x in iris if int(x[4]) == 1]
non_setosa = [Point2D(x[2], x[3]) for x in iris if int(x[4]) != 1]

separator = find_separator(setosa, non_setosa)

if separator:
    print(f"Found separating line: {separator.a}x + {separator.b}y + {separator.c} = 0")

    # Plot result
    x_vals = np.linspace(min([p.x for p in setosa+non_setosa]),
                         max([p.x for p in setosa+non_setosa]), 200)
    y_vals = -(separator.a * x_vals + separator.c) / separator.b

    plt.scatter([p.x for p in setosa], [p.y for p in setosa], c="blue", label="Setosa")
    plt.scatter([p.x for p in non_setosa], [p.y for p in non_setosa], c="orange", label="Non-setosa")
    plt.plot(x_vals, y_vals, "g-", linewidth=2, label="Found separator")

    # Rectangle
    xs = [p.x for p in setosa + non_setosa]
    ys = [p.y for p in setosa + non_setosa]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    rect_x = [min_x, max_x, max_x, min_x, min_x]
    rect_y = [min_y, min_y, max_y, max_y, min_y]
    plt.plot(rect_x, rect_y, "k--", label="Bounding rectangle")

    plt.xlabel("Petal length")
    plt.ylabel("Petal width")
    plt.legend()
    plt.show()
else:
    print("No separating line found (try increasing max_attempts)")
