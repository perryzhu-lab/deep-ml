import numpy as np


def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.

    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation

    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # 计算数值梯度
    # 1. 初始化数值梯度数组
    numerical_grad = np.zeros_like(x, dtype=float)

    # 2. 遍历 x 中的每一个元素
    for i in range(len(x)):
        # 3. 创建两个副本
        x_plus = x.copy()
        x_minus = x.copy()

        # 4. 对第 i 个元素分别进行正负扰动
        x_plus[i] += epsilon
        x_minus[i] -= epsilon

        # 5. 计算扰动后的函数值
        f1 = f(x_plus)
        f2 = f(x_minus)

        # 6. 使用中心有限差分公式计算第 i 个偏导数
        grad = (f1 - f2) / (2 * epsilon)
        numerical_grad[i] = grad

    # 计算相对误差
    numerator = np.linalg.norm(numerical_grad - analytical_grad)
    denominator = np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad)
    if denominator == 0:
        relative_error = 0
    else:
        relative_error = numerator / denominator

    return numerical_grad, relative_error
