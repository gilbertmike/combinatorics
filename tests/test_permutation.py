import unittest

from math import factorial

from combinatorics.permutation import powerset_permutation


class TestPermutation(unittest.TestCase):
    def test_powerset_permutation(self):
        ITEMS = list(range(4))

        num_soln_with_len = {}
        for soln in powerset_permutation(ITEMS):
            len_soln = len(soln)
            if len_soln in num_soln_with_len:
                num_soln_with_len[len_soln] += 1
            else:
                num_soln_with_len[len_soln] = 1

        for len_soln, num_soln in num_soln_with_len.items():
            self.assertEqual(
                factorial(len(ITEMS))/factorial(len(ITEMS)-len_soln),
                num_soln
            )
