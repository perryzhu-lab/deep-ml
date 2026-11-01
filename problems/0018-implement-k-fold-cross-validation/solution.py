import numpy as np
from typing import List, Tuple


def k_fold_cross_validation(
    n_samples: int, k: int = 5, shuffle: bool = True
) -> List[Tuple[List[int], List[int]]]:

    # 1. 生成样本索引
    indices = np.arange(n_samples)

    # 2. 根据 shuffle 决定是否随机打乱
    if shuffle:
        np.random.shuffle(indices)

    # 3. 将索引划分成 k 折
    folds = np.array_split(indices, k)

    # 4. 保存训练集和测试集
    result = []

    for i in range(k):
        # 当前折作为测试集
        test_indices = folds[i]

        # 其他折合并为训练集
        train_indices = np.concatenate(
            [folds[j] for j in range(k) if j != i]
        )

        # 转换为 Python 列表并保存
        result.append((train_indices.tolist(), test_indices.tolist()))

    return result