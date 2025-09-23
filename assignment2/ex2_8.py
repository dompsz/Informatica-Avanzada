import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('../training.txt')

# Extract petal length, petal width, and species
petal_length = iris[:, 2]
petal_width = iris[:, 3]
species = iris[:, 4]

colors = {1: 'red', 2: 'green', 3: 'blue'}
labels = {1: 'Setosa', 2: 'Versicolor', 3: 'Virginica'}

plt.figure(figsize=(8,6))

for s in [1, 2, 3]:
    mask = species == s
    plt.scatter(petal_length[mask], petal_width[mask],
                color=colors[s], label=labels[s], alpha=0.6)

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris Dataset: Petal Length vs Petal Width')
plt.legend()
plt.grid(True)
plt.show()
