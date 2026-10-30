import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    np_x = np.asarray(X, dtype=float)
    A = np_x.T @ np_x
    B = np_x.T @ y

    theta = np.linalg.solve(A, B)

    return np.round(theta, 4).tolist()
