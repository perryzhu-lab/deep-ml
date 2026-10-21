def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    row = len(a)
    col = len(a[0])

    ans = []

    if col != len(b):
        return -1

    for i in range(row):
        num = 0
        for j in range(col):
            num += a[i][j]*b[j]
        ans.append(num)

    return ans