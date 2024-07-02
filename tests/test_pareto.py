from operator import add
import unittest

import numpy as np

from combinatorics.pareto import *


class TestPareto(unittest.TestCase):
    def test_pareto_filter_duplicate_y(self):
        x = np.array([1, 3, 2])
        y = np.array([3, 1, 1])
        self.assertEqual([0, 2], pareto_filter(x, y).tolist())

    def test_pareto_filter_duplicate_x(self):
        x = np.array([1, 3, 2, 3])
        y = np.array([3, 1, 1, 2])
        self.assertEqual([0, 2], pareto_filter(x, y).tolist())


class TestCombineData(unittest.TestCase):
    def test_one_to_one_add(self):
        x1 = np.array([1, 2])
        y1 = np.array([1, 2])

        x2 = np.array([1, 2])
        y2 = np.array([1, 2])

        combined_x, combined_y = combine_data(x1, y1, x2, y2, add, add)

        ref_x_to_y = {2: {2}, 3: {3}, 4: {4}}

        self.check_result(ref_x_to_y, combined_x, combined_y)

    def test_one_to_many_add(self):
        x1 = np.array([1, 2])
        y1 = np.array([2, 1])

        x2 = np.array([1, 2])
        y2 = np.array([2, 2])

        combined_x, combined_y = combine_data(x1, y1, x2, y2, add, add)

        ref_x_to_y = {2: {4}, 3: {3, 4}, 4: {3}}

        self.check_result(ref_x_to_y, combined_x, combined_y)
    
    def test_max(self):
        x1 = np.array([1, 2])
        y1 = np.array([2, 1])

        x2 = np.array([1, 2])
        y2 = np.array([2, 2])

        combined_x, combined_y = combine_data(x1, y1, x2, y2, np.maximum, add)

        ref_x_to_y = {1: {4}, 2: {3, 4}}

        self.check_result(ref_x_to_y, combined_x, combined_y)

    def check_result(self, ref_x_to_y, combined_x, combined_y):
        for i, x in enumerate(combined_x):
            self.assertTrue(combined_y[i] in ref_x_to_y[x])


class TestCombinePareto(unittest.TestCase):
    def test_one_to_many(self):
        x1 = np.array([1, 2])
        y1 = np.array([2, 1])

        x2 = np.array([1, 2])
        y2 = np.array([2, 2])

        combined_x, combined_y = combine_pareto(x1, y1, x2, y2, add, add)

        ref_x_to_y = {2: {4}, 3: {3}}

        self.check_result(ref_x_to_y, combined_x, combined_y)

    def check_result(self, ref_x_to_y, combined_x, combined_y):
        for i, x in enumerate(combined_x):
            self.assertTrue(combined_y[i] in ref_x_to_y[x])