from itertools import permutations
from typing import Iterable

def powerset_permutation(items: Iterable):
    """The permutation of all subset of items (empty set included)."""
    for i in range(len(items)+1):
        yield from permutations(items, i)
