import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:
    # 1. 获取样本数量和特征数量
    m, n = X.shape
    # 2. 初始化模型参数
    theta = np.zeros(n)
    # 3. 梯度下降迭代
    for _ in range(iterations):
        # 计算预测值
        y_pred = X @ theta
        # 计算误差
        error = y_pred - y
        # 计算梯度
        gradient = (X.T @ error) / m
        # 梯度更新
        theta = theta - alpha * gradient

    return theta
