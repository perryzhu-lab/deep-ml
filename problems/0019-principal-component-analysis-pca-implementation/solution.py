import numpy as np


def pca(data: np.ndarray, k: int) -> np.ndarray:
    # 标准化
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standard = (data - mean) / std

    # 计算协方差矩阵
    cov = np.cov(standard, rowvar=False)

    # 特征值分解
    values, vectors = np.linalg.eigh(cov)

    # 选取最大的k个特征值对应的特征向量
    indices = np.argsort(values)[::-1]
    matrix = vectors[:, indices]
    k_matrix = matrix[:, :k]

    # 统一特征向量符号
    for j in range(k):
        vector = k_matrix[:, j]

        indices = np.where(np.abs(vector) > 1e-10)[0]

        if len(indices) > 0:
            first_indice = indices[0]
            if vector[first_indice] < 0:
                vector *= -1

    return np.round(k_matrix, 4)
