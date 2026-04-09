import numpy as np


def gini(values):
    values = np.array(values)
    diff_sum = np.sum(np.abs(values[:, None] - values))
    return diff_sum / (2 * len(values)**2 * np.mean(values))
