def determinant_4x4(matrix: list[list[int | float]]) -> float:
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        nums = 0
        #按第0行展开
        for j in range(n):
            minor = [
                [row[col] for col in range(n) if col!=j]
                for row in matrix[1:]
            ]
            nums += (-1) ** j * matrix[0][j] * determinant_4x4(minor)

        return nums

