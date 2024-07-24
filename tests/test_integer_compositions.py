import unittest

from itertools import product
from math import comb

from combinatorics.integer import *


class TestCompositions(unittest.TestCase):
    def test_integer_compositions(self):
        for n, n_parts in product(range(3, 12), [1, 2, 3]):
            n_solns = 0
            all_solns = set()
            for soln in integer_compositions_with_n_parts(n, n_parts):
                self.assertEqual(n, sum(soln))

                self.assertTrue(soln not in all_solns)
                all_solns.add(soln)

                n_solns += 1
            # See: https://en.wikipedia.org/wiki/Composition_(combinatorics)
            self.assertEqual(comb(n-1, n_parts-1), n_solns)

    def test_weak_integer_compositions(self):
        for n, n_parts in product(range(3, 12), [1, 2, 3]):
            n_solns = 0
            all_solns = set()
            for soln in weak_integer_compositions_with_n_parts(n, n_parts):
                self.assertEqual(n, sum(soln))

                self.assertTrue(soln not in all_solns)
                all_solns.add(soln)

                n_solns += 1
            # See: https://en.wikipedia.org/wiki/Composition_(combinatorics)
            self.assertEqual(comb(n+n_parts-1, n_parts-1), n_solns)

    def test_weak_vector_compositions(self):
        N_PARTS = 3
        for v in product(list(range(4)), list(range(4)), list(range(4))):
            n_solns = 0
            for soln in weak_vector_compositions_with_n_parts(v, N_PARTS):
                self.assertEqual(v, tuple(map(sum, zip(*soln))))
                n_solns += 1
            self.assertEqual(
                reduce(
                    mul,
                    map(lambda comp: comb(comp+N_PARTS-1, N_PARTS-1),
                        v)
                ),
                n_solns
            )
    
    def test_integer_factorizations(self):
        N_PARTS = 3
        for i in range(1, 100):
            for soln in integer_factorizations_to_n_parts(i, N_PARTS):
                self.assertEqual(i, reduce(mul, soln))
