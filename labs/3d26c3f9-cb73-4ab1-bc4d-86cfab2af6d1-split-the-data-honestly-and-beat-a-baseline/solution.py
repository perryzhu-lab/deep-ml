import numpy as np


def split_and_baseline(X, y, train_frac, val_frac, test_frac, seed):
    n, d = X.shape
    rng = np.random.default_rng(seed)
    indices = rng.permutation(n)

    train_end = int(n * train_frac)
    val_end = train_end + int(n * val_frac)

    train_idx = indices[:train_end]
    val_idx = indices[train_end:val_end]
    test_idx = indices[val_end:]

    X_train = X[train_idx]
    y_train = y[train_idx]

    bias = np.ones((len(X_train), 1))
    X_train_bias = np.concatenate((bias, X_train), axis=1)

    theta = np.linalg.lstsq(X_train_bias, y_train, rcond=None)[0]

    X_test = X[test_idx]
    bias = np.ones((len(X_test), 1))
    X_test_bias = np.concatenate((bias, X_test), axis=1)

    test_predictions = X_test_bias @ theta

    return test_predictions, train_idx, val_idx, test_idx
