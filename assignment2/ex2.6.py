import numpy as np
import matplotlib.pyplot as plt

#num_walks = amount of "entities" walking
#seed is set for reproducibility, change for different outcome
def random_walks(num_walks=15, length=1000, seed=5):
    np.random.seed(seed)

    for _ in range(num_walks):
        steps = np.random.normal(0, 1, length - 1)
        walk = np.concatenate(([0], np.cumsum(steps)))
        plt.plot(walk)

    plt.title("Random walks")
    plt.show()

random_walks()
