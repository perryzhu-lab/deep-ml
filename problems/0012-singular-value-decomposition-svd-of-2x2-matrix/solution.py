import numpy as np


def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    # 1. 计算B
    B = A.T @ A

    # 2. jacobi旋转求出V
    theta = np.arctan2(2 * B[0][1], B[0][0] - B[1][1]) / 2

    V = np.zeros_like(B, dtype=float)
    V[0][0] = np.cos(theta)
    V[0][1] = -np.sin(theta)
    V[1][0] = np.sin(theta)
    V[1][1] = np.cos(theta)

    # 3. 计算奇异值σ
    D = V.T @ B @ V
    eigenvalues = np.diag(D)
    sigma = np.sqrt(np.maximum(eigenvalues, 0))
    # 获取奇异值从大到小排列顺序
    indices = np.argsort(sigma)[::-1]
    # 调整奇异值
    sigma = sigma[indices]
    # 调整V的列
    V = V[:, indices]

    # 4. 求出U
    U = np.zeros((2, 2), dtype=float)
    if sigma[0] > 0:
        U[:, 0] = (A @ V[:, 0]) / sigma[0]
    else:
        U[:, 0] = [1.0, 0.0]
    if sigma[1] > 0:
        U[:, 1] = (A @ V[:, 1]) / sigma[1]
    else:
        U[:, 1] = [-U[1, 0], U[0, 0]]

    return (U,sigma,V.T)