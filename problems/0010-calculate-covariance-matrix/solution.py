import numpy as np


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    arr = np.asarray(vectors)
    cov = np.cov(arr, rowvar=True, bias=False)
    return cov.tolist()
