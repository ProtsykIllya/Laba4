import numpy as np
def matrix_stats(size):
    matrix = np.random.rand(size, size)
    return {
        "mean": round(float(matrix.mean()), 3),
        "max": round(float(matrix.max()), 3),
        "det": round(float(np.linalg.det(matrix)), 3),
    }