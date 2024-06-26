from itertools import combinations, permutations

def powerset_permutation(items):
    """The permutation of all subset of items (empty set included)."""
    for i in range(len(items)+1):
        yield from permutations(items, i)
