from functools import reduce
from itertools import combinations, product, starmap
from operator import mul
from typing import Iterable

from .primes import PRIMES


def prime_factorization(x: int):
    """
    Prime factorization of x >= 2 as a list of powers of prime numbers
    listed in PRIMES.
    """
    powers = []
    for p in PRIMES:
        powers.append(0)

        quotient = x // p
        while quotient*p == x:
            powers[-1] += 1
            x = quotient
            quotient = x // p
        
        if x == 1:
            break

    return tuple(powers)


def integer_compositions_with_n_parts(n: int, n_parts: int):
    """Partition integer `n` into positive `n_parts`, which sum to n."""
    if n_parts == 1:
        yield (n,)
        return

    actual_soln = [0]*n_parts
    for soln in combinations(range(1, n), n_parts-1):
        before = 0
        for i in range(len(soln)):
            actual_soln[i] = soln[i] - before
            before = soln[i]
        actual_soln[-1] = n - soln[-1]
        yield tuple(actual_soln)


def weak_integer_compositions_with_n_parts(n: int, n_parts: int):
    """Partition integer n into non-negative n_parts, which sum to n."""
    if n_parts == 1:
        yield (n,)
        return

    n += n_parts # because each part can be zero
    actual_soln = [0 for _ in range(n_parts)]
    for soln in combinations(range(1, n), n_parts-1):
        before = 0
        for i in range(len(soln)):
            actual_soln[i] = soln[i] - before - 1
            before = soln[i]
        actual_soln[-1] = n - soln[-1] - 1
        yield tuple(actual_soln)


def weak_vector_compositions_with_n_parts(v: Iterable, n_parts: int):
    """
    Partition a vector v into n_parts, which sum to v and have
    non-negative components.
    """
    component_choices = [
        weak_integer_compositions_with_n_parts(component, n_parts)
        for component in v
    ]
    for vector_part_choices in product(*component_choices):
        yield tuple(zip(*vector_part_choices))


def integer_factorizations_to_n_parts(n: int, n_parts: int):
    """
    Factorizations of integer n into n_parts (each part is considered distinct,
    as in permutation instead of combinations).
    """
    powers = prime_factorization(n)
    for power_soln in weak_vector_compositions_with_n_parts(powers, n_parts):
        yield tuple(
            reduce(mul, starmap(pow, zip(PRIMES, part_powers)))
            for part_powers in power_soln
        )
