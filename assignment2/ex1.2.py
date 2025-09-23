import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / num_points)
    return pi_estimate


for i in range(1, 6):
    num_points = 10 ** i
    print(f"{num_points} iterations: ", estimate_pi(num_points))
