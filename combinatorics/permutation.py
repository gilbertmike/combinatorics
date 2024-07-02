from itertools import permutations
from typing import Iterable


def powerset_permutation(items: Iterable):
    """The permutation of all subset of items (empty set included)."""
    for i in range(len(items)+1):
        yield from permutations(items, i)


def get_permutation_map(permutation: Iterable, origin: Iterable):
    """Returns a list L such that permutation[i] == origin[L[i]]."""
    result = [None for _ in range(len(permutation))]
    for i, p in enumerate(permutation):
        for j, o in enumerate(origin):
            if p == o:
                result[i] = j
                break
    return result
