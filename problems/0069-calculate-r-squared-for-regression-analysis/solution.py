import numpy as np


def r_squared(y_true, y_pred):
    # 在这里编写你的代码
    ssr = np.sum((y_true - y_pred) ** 2)

    y_mean = np.mean(y_true)
    sst = np.sum((y_true - y_mean) ** 2)

    r2 = 1 - ssr / sst

    return r2