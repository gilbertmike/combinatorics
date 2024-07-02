import unittest
import numpy as np

from combinatorics.pareto import pareto_filter


class TestPareto(unittest.TestCase):
    def test_pareto_filter_duplicate_y(self):
        x = np.array([1, 3, 2])
        y = np.array([3, 1, 1])
        self.assertEqual([0, 2], pareto_filter(x, y).tolist())

    def test_pareto_filter_duplicate_x(self):
        x = np.array([1, 3, 2, 3])
        y = np.array([3, 1, 1, 2])
        self.assertEqual([0, 2], pareto_filter(x, y).tolist())
