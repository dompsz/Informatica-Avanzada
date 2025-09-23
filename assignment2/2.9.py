from ex2_4_and_5 import LinearEquation
from ex2_2 import Point2D

def is_linearly_separable(line, set1, set2):
    # Evaluate the line equation for all points in both sets
    values1 = [line.evaluate(p) for p in set1]
    values2 = [line.evaluate(p) for p in set2]

    # Determine the signs
    set1_positive = all(v > 0 for v in values1)
    set1_negative = all(v < 0 for v in values1)
    set2_positive = all(v > 0 for v in values2)
    set2_negative = all(v < 0 for v in values2)

    # Check separability
    if (set1_positive and set2_negative) or (set1_negative and set2_positive):
        return True
    else:
        return False

setosa_points = [Point2D(1.4, 0.2), Point2D(1.3, 0.2), Point2D(1.5, 0.2)]
non_setosa_points = [Point2D(4.7, 1.4), Point2D(4.5, 1.5), Point2D(5.6, 2.1)]

# Define two example lines
line1 = LinearEquation(0.56, 2.2, -3.5)  # supposed to separate
line2 = LinearEquation(-0.8, 4.3, -3.5)  # supposed not to separate

print(is_linearly_separable(line1, setosa_points, non_setosa_points))  # True
print(is_linearly_separable(line2, setosa_points, non_setosa_points))  # False
