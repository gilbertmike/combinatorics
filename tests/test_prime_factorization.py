import unittest

from functools import reduce
from itertools import starmap
from operator import mul, pow

from combinatorics.integer import prime_factorization
from combinatorics.primes import PRIMES


class TestPrimeFactorization(unittest.TestCase):
    def test_prime_factorization(self):
        for i in range(2, 100):
            self.assertEqual(
                i,
                self.compute_truth(prime_factorization(i))
            )

    @staticmethod
    def compute_truth(powers):
        return reduce(mul, starmap(pow, zip(PRIMES, powers)))
