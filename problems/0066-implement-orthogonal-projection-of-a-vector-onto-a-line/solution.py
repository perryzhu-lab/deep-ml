import numpy as np


def orthogonal_projection(v, L):
    numerator = np.dot(v, L)
    denominator = np.dot(L, L)
    projection = (numerator / denominator) * np.asarray(L)
    return np.round(projection,3).tolist()
    
