import numpy as np


def posterior(X, y, m0, S0, sigma2):
    S0_inv = np.linalg.inv(S0)

    SN = np.linalg.inv(S0_inv + (X.T @ X) / sigma2)

    mN = SN @ (S0_inv @ m0 + (X.T @ y) / sigma2)

    return (mN, SN)


def sequential_posterior(X, y, m0, S0, sigma2):
    m, n = X.shape
    cur_m = m0.copy()
    cur_S = S0.copy()
    means = []
    for i in range(m):
        X_i = X[i : i + 1]
        y_i = y[i : i + 1]

        cur_m, cur_S = posterior(X_i, y_i, cur_m, cur_S, sigma2)

        means.append(cur_m)
    means = np.asarray(means)
    return cur_m, cur_S, means


def predictive(X_test, mN, SN, sigma2):
    mean = X_test @ mN
    var = sigma2 + np.sum((X_test @ SN) * X_test, axis=1)
    return mean, var
