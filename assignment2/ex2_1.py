import numpy as np

class Mean:
    def __init__(self):
        self._count = 0
        self._mean = 0.0

    def new(self, x):
        self._count += 1
        self._mean += (x - self._mean) / self._count

    def value(self):
        return self._mean


v = np.array([2, 7, 5, 7, 18])
m = Mean()

for x in v:
    m.new(x)
    print("Current average:", m.value())

print("Numpy mean:", np.mean(v))
