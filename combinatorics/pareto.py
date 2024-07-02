from typing import Callable, TypeVar

import numpy as np


S = TypeVar('S')
T = TypeVar('T')


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


def combine_pareto(
    x1: np.array,
    y1: np.array,
    x2: np.array,
    y2: np.array,
    x_combiner: Callable,
    y_combiner: Callable
):
    """Returns the combined Pareto curve.
    
    Elements of x are combined as x = x_combiner(e1, e2), e1 in x1, e2 in x2.
    Elements of y are combined similarly.
    Common choices for the combiner are `operator.add` and `max`
    """
    pass
