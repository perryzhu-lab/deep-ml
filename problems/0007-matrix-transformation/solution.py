import numpy as np


def transform_matrix(
    A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
) -> list[list[int | float]]:
    np_A = np.asarray(A, dtype=float)
    np_T = np.asarray(T, dtype=float)
    np_S = np.asarray(S, dtype=float)

    try:
        np.linalg.inv(np_S)
        transformed_matrix = np.linalg.solve(np_T, np_A) @ np_S

    except np.linalg.LinAlgError:
        return -1

    return transformed_matrix.tolist()
