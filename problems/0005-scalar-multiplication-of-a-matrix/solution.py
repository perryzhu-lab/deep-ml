import numpy as np


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    # # python基础语法
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         matrix[i][j] *= scalar
    # return matrix

    # numpy 语法
    arr = np.asarray(matrix)
    return (arr * scalar).tolist()
