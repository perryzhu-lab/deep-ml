import numpy as np


def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # 标准化
    miu=np.mean(data,axis=0)
    sigma=np.std(data,axis=0)
    # 广播机制
    standardization=(data-miu)/sigma
    standardization=np.round(standardization,4)

    # 归一化
    normalization=(data-np.min(data,axis=0))/(np.max(data,axis=0)-np.min(data,axis=0))
    normalization=np.round(normalization,4)

    return (standardization,normalization)