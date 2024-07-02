import unittest

from math import factorial

from combinatorics.permutation import *


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
    

class TestGetPermutationMap(unittest.TestCase):
    def test_one_to_one(self):
        permutation = 'cab'
        origin = 'abc'
        result = get_permutation_map(permutation, origin)
        self.assertEqual([2, 0, 1], result)
    
    def test_missing_element(self):
        permutation = 'cav'
        origin = 'abc'
        result = get_permutation_map(permutation, origin)
        self.assertEqual([2, 0, None], result)
    
    def test_many_to_one(self):
        permutation = 'cabcb'
        origin = 'abc'
        result = get_permutation_map(permutation, origin)
        self.assertEqual([2, 0, 1, 2, 1], result)
    
    def test_many_to_one_and_missing_element(self):
        permutation = 'cabcbv'
        origin = 'abc'
        result = get_permutation_map(permutation, origin)
        self.assertEqual([2, 0, 1, 2, 1, None], result)
        
