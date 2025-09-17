import numpy as np

def trapezoidal_rule(f, a, b, N=1000):
    x = np.linspace(a, b, N + 1)
    y = f(x)
    dx = (b - a) / N
    return (dx / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def P(t):
    return 1 / (1 + np.exp(-t))

#a, b are variables for the function. N is the number of trapezoids
approx = trapezoidal_rule(P, -21, 37, 25)
print("Approximate integral:", approx)
