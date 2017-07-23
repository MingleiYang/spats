import unittest

from spats_shape_seq import Spats
from spats_shape_seq.pair import Pair


# [ id, r1, r2, end, site ]
cases = [
    [ "1116:19486:8968", "TCCGGTCCTTGGTGCCCGAGTCAGTCCTTCCTCCTA", "GAGTCTATTTTTTTAGGAGGAAGGACTGACTCGGGC", 93, 68 ],
]

class TestPairs(unittest.TestCase):

    def setUp(self):
        self.spats = Spats()
        self.spats.run.cotrans = True
        self.spats.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
        self.spats.addTargets("test/cotrans/cotrans_single.fa")

    def tearDown(self):
        self.spats = None

    def pair_for_case(self, case):
        pair = Pair()
        pair.set_from_data(case[0], case[1], case[2])
        return pair

    def run_case(self, case):
        pair = self.pair_for_case(case)
        self.spats.process_pair(pair)
        self.assertEqual(case[3], pair.end)
        self.assertEqual(case[4], pair.site)
        return pair

    def test_pairs(self):
        for case in cases:
            self.run_case(case)
        print "Ran {} pair->site cases.".format(len(cases))
