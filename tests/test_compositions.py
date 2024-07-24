import unittest

from combinatorics.compositions import compositions_of_sequence


class TestCompositions(unittest.TestCase):
    def test_compositions_of_set(self):
        ITEMS = 'abcd'

        all_solns = set()
        for composition in compositions_of_sequence(ITEMS):
            self.assertEqual(ITEMS, ''.join(composition))

            self.assertTrue(composition not in all_solns)
            all_solns.add(composition)

        # See: https://en.wikipedia.org/wiki/Composition_(combinatorics)
        self.assertEqual(2**(len(ITEMS)-1), len(all_solns))
