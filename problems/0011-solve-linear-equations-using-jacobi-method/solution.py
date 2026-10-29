import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    # 初始化解向量
    x = np.zeros(len(b))
    # 提取对角线元素
    diag = np.diag(A)

    # 计算新一轮的x
    for _ in range(n):
        # x用来保存上一轮的结果
        new_x = np.zeros_like(x)
        # 计算new_x[0],new_x[1],...
        for i in range(len(b)):
            a_ii = diag[i]
            b_i = b[i]
            nums = 0
            for j in range(len(b)):
                if j == i:
                    continue
                nums += A[i][j] * x[j]
            new_x[i] = (b_i - nums) / a_ii

        x = new_x

    return np.round(x, 4).tolist()
