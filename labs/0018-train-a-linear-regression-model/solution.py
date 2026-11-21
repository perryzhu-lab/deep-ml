
import numpy as np

def train(X, y, W, b):
    # 1. 获取样本数量
    n_samples, n_features = X.shape

    # 2. 设置超参数
    lr = 0.01
    iterations = 10000

    # 复制初始权重
    W = W.copy()

    # 3. 梯度下降
    for _ in range(iterations):

        # 计算预测值
        y_pred = X @ W + b

        # 计算误差
        error = y_pred - y

        # 计算梯度
        gradient_W = (2 / n_samples) * (X.T @ error)
        gradient_b = 2 * np.mean(error)

        # 更新权重与偏置
        W -= lr * gradient_W
        b -= lr * gradient_b

    return W, b
