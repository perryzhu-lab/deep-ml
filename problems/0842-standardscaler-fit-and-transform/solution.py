import numpy as np


def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    
    n_train, n_features = X_train.shape
    miu = np.mean(X_train, axis=0)
    sigma = np.std(X_train, axis=0)

    sigma[sigma == 0] = 1
    return (X_test - miu) / sigma
