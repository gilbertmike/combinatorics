from itertools import product
import unittest

from combinatorics.dependent_product import dependent_product
from combinatorics.splitter import split_dependent_product


class TestSplitDependentProduct(unittest.TestCase):
    def test_split_dependent_product(self):
        spaces = [
            lambda: [(i,) for i in range(3)],
            lambda x: [(x, i) for i in range(3)],
            lambda x, y: [(x, y, i) for i in range(3)],
        ]
        spaces1, spaces2 = split_dependent_product(4, spaces)
        spaces1_points = set(dependent_product(spaces1))
        self.assertEqual(spaces1_points,
                         set(product(range(3), repeat=2)))
        self.assertEqual(len(spaces1) + len(spaces2), len(spaces))
