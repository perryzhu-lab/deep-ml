def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    row = len(matrix)
    col = len(matrix[0])
    means = []
    # 记录行和和列和
    rows = []
    cols = []

    for i in range(row):
        nums = 0
        for j in range(col):
            nums += matrix[i][j]
        rows.append(nums)

    for j in range(col):
        nums = 0
        for i in range(row):
            nums += matrix[i][j]
        cols.append(nums)

    if mode == 'row':
        for i in range(row):
            means.append(rows[i]/col)

    if mode =='column':
        for j in range(col):
            means.append(cols[j]/row)

    return means
