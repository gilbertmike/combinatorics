from collections.abc import Callable, Sequence

from combinatorics.dependent_product import dependent_product


def split_dependent_product(n_split_min: int, spaces: Sequence[Callable]):
    """
    Splits spaces into two such that the first set of spaces is the smallest
    set of spaces that has number of points >= `n_split_min`.
    """
    for i in range(1, len(spaces)):
        splits = list(dependent_product(spaces[:i]))
        if len(splits) >= n_split_min:
            return spaces[:i], spaces[i:]
