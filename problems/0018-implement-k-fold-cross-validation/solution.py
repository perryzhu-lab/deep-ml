import numpy as np
from typing import List, Tuple


def k_fold_cross_validation(
    n_samples: int, k: int = 5, shuffle: bool = True
) -> List[Tuple[List[int], List[int]]]:
    # n_samples: int                        样本总数。
    # k: int = 5                            默认划分为 5 折。
    # shuffle: bool = True                  默认随机打乱索引。
    # List[Tuple[List[int], List[int]]]     返回一个列表，里面每个元素都是 (训练集索引列表, 测试集索引列表)

    # 1. 生成索引
    indices = np.arange(n_samples)

    # 2. 随机打乱
    if shuffle:
        np.random.shuffle(indices)

    # 3. 划分k折
    folds = np.array_split(indices, k)

    
    # 4. 轮流选择测试集
    res=[]
    for i in range(k):
        test_indices = folds[i]
        train_indices = np.concatenate([folds[j] for j in range(k) if j != i])
        res.append((train_indices.tolist(),test_indices.tolist()))

    # 5. 保存结果
    return res
