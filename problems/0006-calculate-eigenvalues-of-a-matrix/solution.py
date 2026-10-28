import numpy as np


def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    # # python基础语法
    # ans = []
    # tr_matrix = matrix[0][0] + matrix[1][1]
    # det_matrix = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # delta = (tr_matrix**2 - 4 * det_matrix) ** 0.5
    # ans.append((tr_matrix - delta) / 2)
    # ans.append((tr_matrix + delta) / 2)
    # ans.sort(reverse=True)
    # return ans

    # numpy语法
    arr = np.asarray(matrix)

    eigenvalues = np.linalg.eigvals(arr)

    return np.sort(eigenvalues)[::-1].tolist()
