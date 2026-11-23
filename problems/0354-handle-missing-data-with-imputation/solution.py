import numpy as np


def impute_missing_data(data, strategy="mean"):
    # 1. 获取数据的行数和列数
    n, d = data.shape

    # 2. 遍历每一列
    for i in range(d):
        # 3. 筛选非缺失值
        mask = np.isnan(data[:, i])
        # 4. 如果整列都是 NaN，跳过
        if np.all(mask):
            continue

        # 5. 根据 strategy 计算填充值并替换
        if strategy == "mean":
            mean = np.nanmean(data[:, i])
            data[mask, i] = mean
        elif strategy == "median":
            median = np.nanmedian(data[:, i])
            data[mask, i] = median
        elif strategy == "mode":
            val, cnt = np.unique(data[~mask, i], return_counts=True)
            index = np.argmax(cnt)
            mode = val[index]
            data[mask, i] = mode
    # 6. 返回处理后的数据
    return data
