import numpy as np


def pca(data: np.ndarray, k: int) -> np.ndarray:
    n_samples = len(data)
    n_features = len(data[0])
    # 1. 数据标准化
    # 计算每个特征的均值和标准差
    # 对每一列进行标准化
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    # 2. 计算协方差矩阵
    # 注意 rowvar=False
    cov = np.cov(standardized_data, rowvar=False)

    # 3. 特征值分解
    # 使用 np.linalg.eigh()
    eigenvalues, eigenvectors = np.linalg.eigh(cov)

    # 4. 按特征值从大到小排序
    # 使用 np.argsort()
    indices = np.argsort(eigenvalues)[::-1]
    matrix = eigenvectors[:, indices]

    # 5. 选择前 k 个主成分
    # 注意特征向量按列存储
    k_matrix = matrix[:, :k]

    # 6. 统一特征向量的符号
    # 遍历每一个主成分
    # 找到第一个绝对值 > 1e-10 的元素
    # 如果该元素为负数，将整列乘以 -1
    for j in range(k):
        v = k_matrix[:, j]

        indices = np.where(np.abs(v) > 1e-10)[0]

        if len(indices) > 0:
            first_index = indices[0]
            if v[first_index] < 0:
                k_matrix[:, j] *= -1

    # 7. 保留 4 位小数并返回
    return np.round(k_matrix, 4)
