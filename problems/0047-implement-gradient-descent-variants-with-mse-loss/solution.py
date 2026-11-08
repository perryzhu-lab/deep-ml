import numpy as np


def gradient_descent(
    X, y, weights, learning_rate, n_epochs, batch_size=1, method="batch"
):
    # 提取样本数量和特征数量
    m, n = X.shape

    # 训练n_epochs轮次
    for _ in range(n_epochs):
        # 批量梯度下降（Batch GD）
        # 每个 epoch 使用全部样本计算一次梯度，并进行一次参数更新。
        if method == "batch":
            # 1. 计算预测值
            y_pred = X @ weights
            # 2. 计算误差
            error = y_pred - y
            # 3. 计算梯度
            gradient = (2 / m) * X.T @ error
            # 4. 更新 weights
            weights = weights - learning_rate * gradient

        # 随机梯度下降（Stochastic GD）
        # 按照顺序逐个处理样本，例如先处理样本 0，再处理样本 1，然后处理样本 2，以此类推
        # 不能随机选择样本。
        elif method == "stochastic":
            for i in range(m):
                y_pred = X[i] @ weights
                error = y_pred - y[i]
                gradient = 2 * X[i].T * error
                weights = weights - learning_rate * gradient

        # 小批量梯度下降（Mini-Batch GD）
        # 按照样本原始顺序，将连续样本划分为互不重叠的小批次
        # 例如，当 batch_size = 2 时，第一个批次使用索引 [0, 1]，第二个批次使用索引 [2, 3]，以此类推
        elif method == "mini_batch":
            for start in range(0, m, batch_size):
                end = start + batch_size
                # 获取当前batch的数据
                X_batch = X[start:end]
                y_batch = y[start:end]
                num = len(X_batch)
                y_pred = X_batch @ weights
                error = y_pred - y_batch
                gradient = (2 / num) * X_batch.T @ error
                weights = weights - learning_rate * gradient

    return weights
