import numpy as np


def rmse(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise ValueError
    if y_true.size == 0 or y_pred.size == 0:
        raise ValueError

    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))

    return np.round(rmse, 3)
