from ex2_4_and_5 import LinearEquation
from ex2_2 import Point2D
import numpy as np
import matplotlib.pyplot as plt

def is_linearly_separable(line, set1, set2):

    vals1 = [line.evaluate(p) for p in set1]
    vals2 = [line.evaluate(p) for p in set2]

    if all(v > 0 for v in vals1) and all(v < 0 for v in vals2):
        return True
    if all(v < 0 for v in vals1) and all(v > 0 for v in vals2):
        return True

    return False


iris = np.loadtxt("../training.txt")

setosa = [Point2D(x[2], x[3]) for x in iris if int(x[4]) == 1]
non_setosa = [Point2D(x[2], x[3]) for x in iris if int(x[4]) != 1]

# Example lines
line1 = LinearEquation(0.56, 2.2, -3.5)   # supposed to separate
line2 = LinearEquation(-0.8, 4.3, -3.5)   # does not separate

print("Line1 separates?", is_linearly_separable(line1, setosa, non_setosa))  # True
print("Line2 separates?", is_linearly_separable(line2, setosa, non_setosa))  # False

x_vals = np.linspace(0, 7, 200)

# ax + by + c = 0  =>  y = -(ax + c)/b
y_line1 = -(line1.a * x_vals + line1.c) / line1.b
y_line2 = -(line2.a * x_vals + line2.c) / line2.b

plt.scatter([p.x for p in setosa], [p.y for p in setosa], c="blue", label="Setosa")
plt.scatter([p.x for p in non_setosa], [p.y for p in non_setosa], c="orange", label="Non-setosa")
plt.plot(x_vals, y_line1, "g-", label="Line1 (separates)")
plt.plot(x_vals, y_line2, "r--", label="Line2 (not separable)")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.legend()
plt.show()
