import numpy as np


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    try:
        inv = np.linalg.inv(arr)
    except np.linalg.LinAlgError:
        return None

    return inv.tolist()
