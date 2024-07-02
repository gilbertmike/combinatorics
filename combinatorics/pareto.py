import numpy as np


def pareto_filter(x: np.array, y: np.array) -> np.array:
    """
    Returns a mask that if applied to x and y returns the Pareto curve
    (defined as lower is better).
    """
    sort_mask = x.argsort()
    y = y[sort_mask]

    running_min_y = np.minimum.accumulate(y)

    filter_mask = np.ones_like(y).astype(np.bool_)
    filter_mask[1:] = y[1:] < running_min_y[:-1]

    return sort_mask[filter_mask]