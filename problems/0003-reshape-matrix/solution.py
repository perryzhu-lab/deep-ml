def reshape_matrix(
    a: list[list[int | float]],
    new_shape: tuple[int, int]
) -> list[list[int | float]]:
    row = new_shape[0]
    col = new_shape[1]

    if len(a) * len(a[0]) != row * col:
        return []

    # python基础语法实现
    nums = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            nums.append(a[i][j])

    b = [[0] * col for _ in range(row)]

    index = 0
    for i in range(row):
        for j in range(col):
            b[i][j] = nums[index]
            index += 1
            
    return b
