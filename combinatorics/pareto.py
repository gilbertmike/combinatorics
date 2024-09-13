from typing import Callable, TypeVar

import numpy as np


S = TypeVar('S')
T = TypeVar('T')


def pareto_filter(x: np.array, y: np.array, impute_y=False) -> np.array:
    """
    Returns a mask that if applied to x and y returns the Pareto curve
    (defined as lower is better).
    """
    sort_mask = x.argsort()
    y = y[sort_mask]

    running_min_y = np.minimum.accumulate(np.nan_to_num(y, nan=np.inf))
    if impute_y:
        return running_min_y

    filter_mask = np.ones_like(y).astype(np.bool_)
    filter_mask[1:] = y[1:] < running_min_y[:-1]
    filter_mask[0] = not np.isnan(y[0])

    return sort_mask[filter_mask]


def combine_data(
    x1: np.array,
    y1: np.array,
    x2: np.array,
    y2: np.array,
    x_combiner: Callable,
    y_combiner: Callable
):
    """Returns the combined points.
    
    Elements of x are combined as x = x_combiner(e1, e2), e1 in x1, e2 in x2.
    Elements of y are combined similarly.
    Common choices for the combiner are `operator.add` and `max`
    """
    x1_shape = x1.shape[0]
    x2_shape = x2.shape[0]

    all_x = np.zeros(x1_shape*x2_shape)
    all_y = np.zeros(x1_shape*x2_shape)

    def make_repeated(x, n):
        return np.tile(x, n).reshape((-1, n)).T.flatten()

    def make_repeated_and_rolled(x, n):
        x_shape = x.shape[0]
        repeated_x = np.zeros((x_shape*n,))
        for i in range(n):
            repeated_x[i*x_shape:(i+1)*x_shape] = np.roll(x, i)
        return repeated_x

    # Compute all pairings
    repeated_x1 = make_repeated(x1, x2_shape)
    repeated_y1 = make_repeated(y1, x2_shape)
    repeated_x2 = make_repeated_and_rolled(x2, x1_shape)
    repeated_y2 = make_repeated_and_rolled(y2, x1_shape)
    
    all_x = x_combiner(repeated_x1, repeated_x2)
    all_y = y_combiner(repeated_y1, repeated_y2)

    return all_x, all_y


def combine_pareto(
    x1: np.array,
    y1: np.array,
    x2: np.array,
    y2: np.array,
    x_combiner: Callable,
    y_combiner: Callable
):
    """Returns the combined and Pareto-filtered curve.
    
    Elements of x are combined as x = x_combiner(e1, e2), e1 in x1, e2 in x2.
    Elements of y are combined similarly.
    Common choices for the combiner are `operator.add` and `max`
    """
    all_x, all_y = combine_data(x1, y1, x2, y2, x_combiner, y_combiner)
    mask = pareto_filter(all_x, all_y)
    return all_x[mask], all_y[mask]
