from collections.abc import Sequence
from itertools import combinations


def compositions_of_sequence(items: Sequence):
    """
    Iterates over all sets of non-overlapping, covering, contiguous
    subsequences of `items`.

    E.g., for ABC, it will iterate over four results:
        A, B, C
        AB, C
        A, BC
        ABC
    """
    for n_parts in range(1, len(items)+1):
        compositions = [None]*n_parts
        for dividers in combinations(range(1, len(items)), n_parts-1):
            last = 0
            for i, divider in enumerate(dividers):
                compositions[i] = items[last:divider]
                last = divider
            compositions[-1] = items[last:]
            yield tuple(compositions)
