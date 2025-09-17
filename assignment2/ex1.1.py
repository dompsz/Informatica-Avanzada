import numpy as np

def all_rows_equal(matrix):
    return np.all(matrix == matrix[0])

A = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [1, 2, 3]])

print(all_rows_equal(A))  # True
print(all_rows_equal(B))  # False
