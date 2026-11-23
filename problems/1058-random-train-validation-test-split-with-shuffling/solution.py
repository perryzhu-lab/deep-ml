import numpy as np


def random_split(
    data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123
) -> list:
    n, d = data.shape
    rng = np.random.default_rng(seed)
    indices = rng.permutation(n)
    shuffled_data = data[indices]

    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    training_set = shuffled_data[:train_end]
    validation_set = shuffled_data[train_end:validation_end]
    test_set = shuffled_data[validation_end:]

    return [training_set, validation_set, test_set]
