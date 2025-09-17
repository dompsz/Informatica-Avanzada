import numpy as np

def trapezoidal_rule(func, a, b, N=1000):
    dx = (b - a) / N
    total = 0.5 * (func(a) + func(b))  # końce z wagą 1/2

    for k in range(1, N):
        x = a + k * dx
        total += func(x)

    return dx * total


def P(t):
    return 1 / (1 + np.exp(-t))

#a, b are variables for the function. N is the number of trapezoids
print(trapezoidal_rule(lambda x: 1 / (1 + np.exp(-x)), -100, 100))
print(trapezoidal_rule(np.sin, 0, np.pi * 2))
print(trapezoidal_rule(lambda x: 1 / (np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2), -10, 10))

#This task was hard to understand even though i have done that one before 👍