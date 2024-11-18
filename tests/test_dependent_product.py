import unittest

from combinatorics.dependent_product import dependent_product


class TestDependentProduct(unittest.TestCase):
    def test_return_tuple(self):
        spaces = [
            lambda: [(i,) for i in range(3)],
            lambda i: [(j,) for j in range(i)],
            lambda i: [(j,) for j in range(i)]
        ]
        result = list(dependent_product(spaces))
        self.assertEqual(result, [(0,)])

    def test_return_single_object(self):
        spaces = [
            lambda: list(range(3)),
            lambda i: list(range(i)),
            lambda i: list(range(i))
        ]
        result = list(dependent_product(spaces))
        self.assertEqual(result, [0])

    def test_return_mixed(self):
        spaces = [
            lambda: list(range(3)),
            lambda i: [(i, j) for j in range(i)],
            lambda i, j: list(range(j))
        ]
        result = list(dependent_product(spaces))
        self.assertEqual(result, [0])
