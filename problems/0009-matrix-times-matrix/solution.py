import numpy as np


def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    np_a = np.asarray(a)
    np_b = np.asarray(b)

    try:
        mul = np_a @ np_b

    except ValueError:
        return -1

    return mul.tolist()
