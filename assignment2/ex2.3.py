import random
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    return 4 * (inside_circle / num_points)

sample_sizes = list(range(5, 4005, 10))
estimates = [estimate_pi(n) for n in sample_sizes]

plt.figure(figsize=(8, 5))
plt.plot(sample_sizes, estimates, marker='o', linestyle='-', label="Estimate of π")
plt.axhline(y=3.14159, color='red', linestyle='--', label="Actual π")

plt.xlabel("Sample size (number of points)")
plt.ylabel("Estimate of π")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.grid(True)
plt.show()
