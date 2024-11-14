import unittest

from combinatorics.dependent_product import dependent_product


class TestDependentProduct(unittest.TestCase):
    def test_dependent_product(self):
        spaces = [
            lambda: [(i,) for i in range(3)],
            lambda i: [(j,) for j in range(i)],
            lambda i: [(j,) for j in range(i)]
        ]
        result = list(dependent_product(spaces))
        self.assertEqual(result, [(0,)])
