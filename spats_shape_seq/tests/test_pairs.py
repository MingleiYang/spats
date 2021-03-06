import unittest

from spats_shape_seq.pair import Pair


cases = [
    [ "1101:11562:1050", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "CCACCTGACCCCATGCCGAACTCAGAAGTGAAACG", 29 ],
    [ "1101:20069:1063", "TTTAGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "TCCCACCTGACCCCATGCCGAACTCAGAAGTGAAA", 27 ],
    [ "21189", "TTTGGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA", "CTGACTCGGGCACCAAGGACCAAAAGATCGGAAGA", 123 ],
    [ "18333", "GAGTGTCCTTGGTGCCCGAGTCAGTGGTAGATCGG", "ACCACTGACTCGGGCACCAAGGACACTCAGATCGG", None ],
    [ "1101:10021:3261", "AAGCGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "CCTGACCCCATGCCGAACTCAGAAGTGAAACCCCG", None ],
    [ "1101:10505:2593", "TCTGGTCCTTGGTGCCCGAGTAGATCGGAAGAGAC", "ACTCGGGCACCAAGGACCAGAAGATCGGAAGAGCG", None ],
    [ "1109:9248:13419", "AGATGTCCTTGGTGCCCGAGTCAGAAGATCGGGAA", "TCTGACTCGGGCACCAAGGACATCTAGATCGGAAG", None ],
    [ "1101:10051:23846", "CTTAGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA", "CTGACTCGGGCACCAAGGACTAAGAGATCGGAAAA", None ],
    [ "1101:13433:5831", "TTCAGTCCTTGGTGCCCGAGTCAGATAGATCGGAA", "ATCTGACTCGGGCACCAAGGACTGAAAGATCGAAA", None ],
    [ "1102:6599:2593", "AAGTGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA", "CTGACTCGGGCACCAAGGACACTTAGATCGGAGAC", None ],
    [ "1101:12888:8140", "GGATGTCCTTGGTGCCCGAGTCAGATGCCAGATCG", "GGCATCTGACTCGGGCACCAAGGACATACAGATCG", 118 ],
    [ "1101:10652:13566", "GAATGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "CCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATG", 64 ], # tests for matching the wrong substring if your min_len
    [ "1101:13864:21135", "GGGTGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "GCCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCAT", 63 ], # is too small and you don't keep looking in find_partial
    [ "1101:11920:1274", "CTTAGTCCTTGGTGCCCGAGTCAGCTTGGTGCCCG", "GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACCT", None ], # similarly if you don't keep checking all sites

    ['jjb_1', 'TCTGAGATCGGAAGAGCACACGTCTGAACTCCAGT', 'CAGAAGATCGGAAGAGCGTCGTGTAGGGAAAGAGT', None ], # R1 is pure adapter, make sure it's rejected
    ['10552', 'CTTAGTCCTTGGTGCCCGAGTCAGCAGATCGGAAG', 'TCTGACTCGGGCACCAAGGACTAAGAGATCGGAAG', None ],

    # various cases which differed with v102
    [ "1101:10582:1913", "AAACGTCCTTGGTGCCCGAGTCAGAGATCGAAGAG", "CTGACTCGGGCACCAAGGGCGTGTATATCGGAAGA", None ],
    [ "1101:12888:8140", "GGATGTCCTTGGTGCCCGAGTCAGATGCCAGATCG", "GGCATCTGACTCGGGCACCAAGGACATACAGATCG", 118 ],
    [ "1101:13433:5831", "TTCAGTCCTTGGTGCCCGAGTCAGATAGATCGGAA", "ATCTGACTCGGGCACCAAGGACTGAAAGATCGAAA", None ],
    [ '1101:15138:1004', 'NTTAGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG', 'NCCGAACTCAGAAGTGAANCGCCGTAGCGCNGANG', None ],
    [ '2119:9713:17009', 'TTCGGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG', 'GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCTCCT', None ],
    [ "1102:6599:2593", "AAGTGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA", "CTGACTCGGGCACCAAGGACACTTAGATCGGAGAC", None ],
    [ '1114:24625:21410', 'AAACGTCCTTGGTGCCCGAGTCAATCGGAAGAGCA', 'ACTCGGGCACCAAGGACGCTTAGATCGGAAGAGCG', None ],
    [ '1109:25722:16247', 'CTCAGTCCTTGGTGCCCGAGTCAATCGGAAGAGCA', 'ACTCGGGCACCAAGGACTGAGAGATCGGCAGAGCG', None ],
    [ '1110:22635:4995', 'TTTAGTCCTTGGTGCCCGAGATCGGAAGAGCACAC', 'CGGGCACCAAGGACTAAAAGATCGGAAGAGCGTCG', 129 ],
    [ '1101:13433:5831', 'TTCAGTCCTTGGTGCCCGAGTCAGATAGATCGGAA', 'ATCTGACTCGGGCACCAAGGACTGAAAGATCGAAA', None ],
    [ '1113:10835:22556', 'AAGTGTCCTTGGTGCCCGAGTCAGATAGATCGGAA', 'ATCTGACTCGGGCACCAAGGACACTTAGATCGGAA', 121 ],
    [ '1103:19743:16573', 'GAGTGTCCTTGGTGCCCGAGTATCGGAAGAGCACA', 'CGGGCACCAAGGACACTCAGATCGGAAGAGCGTCG', None ],
    [ '1101:15979:21832', 'GAATGTCCTTGGTGCCCGAGTCAGATGCAGAACGG', 'GCATCTGACTCGGGCACCAAGGACATTCAGATCGG', None ],
    [ '1101:10344:11542', 'TCTAGTCCTTGGTGCCCGAGTCAGATGCCTGAGAT', 'CAGGCATCTGACTCGGGCACCAAGGACTAGAAGAT', 116 ],
    [ '1101:11816:8298', 'CCCGGTCCTTGGTGCCCGAGTCAGATGCAGATCGG', 'GCATCTGACTCGGGCACCAAGGACCGGGAGATCGG', 119 ],
    [ '1101:11998:14960', 'AGACGTCCTTGGTGCCCGAGTCAGATGCAGATCGG', 'GCATCTGACTCGGGCACCAAGGACGTCTAGATCGG', 119 ],
    [ '1101:25841:19393', 'CTTAGTCCTTGGTGCCCGAGTCAGAGACCGGAAGA', 'CTGACTCGGGCACCAAGGACTAAGGGAGCGGAAGA', None ],
    [ '1102:14595:1033', 'NTCAGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG', 'GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACNT', None ],
    [ '2116:14830:22969', 'CTCAGTCCTTGGTGCCCGAGTCAGGATCGGAAGAG', 'TGACTCGGGCACCAAAGACTGAGAGATCGGAAGAG', None ],
    [ '1101:10344:11542', 'TCTAGTCCTTGGTGCCCGAGTCAGATGCCTGAGAT', 'CAGGCATCTGACTCGGGCACCAAGGACTAGAAGAT', 116 ],
    [ '1115:24186:4558', 'TTTGGTCCTTGGTGCCCGAGTAGATCGGAAGAGCA', 'ACTCGGGCACCAAAGACCAAAAGATCGGAAGAGCG', None ],
    [ '1108:11212:15952', 'TTTGGTCCTTGGTGCCCGAGTCAGAGACGGAAGAG', 'CTGACTCGGGCACCAAGGACCAAAAGATCGGAAGA', None ],
    [ '1107:6287:7763', 'TCTGGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA', 'CTGACTCGGGCACCAAGGACCAGAAGATCGAAGAG', None ],
    [ '1102:16621:23746', 'TCCAGTCCTTGGTGCCCGAGTCAGGATCGGAAGAG', 'TGACTCGGGCACCAAGGCCTGGAAGAACGGAAGAA', None ],
    [ '1102:27276:10366', 'TTTAGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA', 'CTGACTCGGGCACCAAGGACTAAAAGATTGGAAAA', None ],
    [ '1105:12183:24798', 'AGATGTCCTTGGTGCCCGAGTCAGATCGGAAGAGC', 'GACTCGGGCACCAAGGACATCTAGATCGGAAAACC', None ],
    [ '1105:28564:18308', 'CTTAGTCCTTGGTGCCCGAGTAGATCGGAAGAGCA', 'ACTCGGGCACCAAGGACTAAGGGATAGGAAGAGCG', None ],
    [ '1109:14013:17918', 'GGGTGTCCTTGGTGCCCGAGTCAGATGCCTAGATC', 'AGGCATCTGACTCGGGCACCAAGGCCACCCAGATC', None ],
    [ '1116:21540:21211', 'AGATGTCCTTGGTGCCCGAGTCAGATGCCTGAGAT', 'CAGGCATCTGACTCGGGCACCAAGCACATCTAGAT', None ],
    [ '2104:18173:12075', 'AAGCGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG', 'ACTGCCAGGCATCTGACTCGGGCACCAAGGGCGCT', None ],
    [ '2113:28288:17700', 'TCCGGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG', 'AACTGCCAGGCATCTGACTCGGGCACCAACGACCG', None ],
    [ '2118:26021:18628', 'TTTAGTCCTTGGTGCCCGAGTCAGATGCCTGGCAA', 'TGCCAGGCATCTGACTCGGGCACCAAGGCCTAAAA', None ],
    [ '1114:21343:8367', 'TTCAGTCCTTGGTGCCCGAGTGATCGGAAGAGCAC', 'CTCGGGCACCAAGGACTGAAAGCTCGGAAGAGCGA', None ],    

]


class TestPairs(unittest.TestCase):

    def setUp(self):
        from spats_shape_seq import Spats
        self.spats = Spats()
        self.spats.addTargets("test/5s/5s.fa")

    def tearDown(self):
        self.spats = None

    def pair_for_case(self, case):
        pair = Pair()
        pair.set_from_data(case[0], case[1], case[2])
        return pair

    def run_case(self, case):
        pair = self.pair_for_case(case)
        self.spats.process_pair(pair)
        self.assertEqual(case[3], pair.site, "res={} != {} ({}, {})".format(pair.site, case[3], self.__class__.__name__, case[0]))
        return pair

    def test_pairs(self):
        for case in cases:
            self.run_case(case)
        print("Ran {} pair->site cases.".format(len(cases)))

    def test_find_partial_weird_case(self):
        pair = Pair()
        pair.set_from_data("x", 'CTCAGTCCTTGGTGCCCGAGTCAGGATCGGAAGAG', 'TGACTCGGGCACCAAAGACTGAGAGATCGGAAGAG')
        self.spats.process_pair(pair)
        print("{} / {}".format(pair.site, pair.failure))

    def test_minimum_length(self):
        from spats_shape_seq import Spats
        self.spats = Spats()
        self.spats.run.algorithm = "find_partial"
        self.spats.run.minimum_target_match_length = 11
        self.spats.addTargets("test/5s/5s.fa")
        self.assertEqual(11, self.spats._targets.minimum_match_length)
        case = [ '1109:22737:14675', 'TCCAGTCCTTGGAGATCGGAAGAGCACACGTCTGA', 'CCAAGGACTGGAAGATCGGAAGAGCGTCGTGTAGG', None ]
        self.run_case(case)

        # this case only matches if the minimum length is set to 8
        self.spats.run.minimum_target_match_length = 8
        self.spats = Spats()
        self.spats.run.algorithm = "lookup"
        self.spats.addTargets("test/5s/5s.fa")
        case[3] = 135
        self.run_case(case)


# run all the same tests with a targets file that has 'U' instead of 'T'
class TestPairsWithU(TestPairs):

    def setUp(self):
        from spats_shape_seq import Spats
        self.spats = Spats()
        self.spats.addTargets("test/5s/5su.fa")


class TestPanelPairs(unittest.TestCase):

    def setUp(self):
        from spats_shape_seq import Spats
        self.spats = Spats()
        self.spats.run.minimum_target_match_length = 10
        self.spats.addTargets("test/panel_RNAs/panel_RNAs_complete.fa")

    def tearDown(self):
        self.spats = None

    def test_single_R1_match_with_adapter_multiple_without(self):
        pair = Pair()
        pair.set_from_data('M02465:8:000000000-A5D', 'CCCGCCGTCCTTGGTGCCCGAGTGAGATCGGAAGA','CACTCGGGCACCAAGGACGGCGGGAGATCGGAAGA')
        self.spats.run.debug = True
        self.spats.run.algorithm = "find_partial"
        self.spats.process_pair(pair)
        self.assertEqual(None, pair.target)
        self.assertEqual(1, self.spats.counters.multiple_R1_match)


prefix_cases = [
    [ "p1", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACCT", 0, '' ],
    [ "*p2", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "TGGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACC", 0, 'T' ],
    [ "p3", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "TTGGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACC", 0, 'TT' ],
    [ "p4", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "ACGTGGATGCCTGGCGGCCGTAGCGCGGTGGTCCCA", 0, 'ACGT' ],
]

class TestPrefixPairs(unittest.TestCase):

    def setUp(self):
        from spats_shape_seq import Spats
        self.spats = Spats()
        self.spats.run.collapse_left_prefixes = True
        self.spats.addTargets("test/5s/5s.fa")

    def tearDown(self):
        self.spats = None

    def pair_for_case(self, case):
        pair = Pair()
        pair.set_from_data(case[0], case[1], case[2])
        return pair

    def run_case(self, case):
        pair = self.pair_for_case(case)
        self.spats.counters.reset()
        self.spats.process_pair(pair)
        self.assertEqual(case[3], pair.site, "res={} != {} ({}, {})".format(pair.site, case[3], self.__class__.__name__, case[0]))
        if case[4]:
            self.assertEqual(1, getattr(self.spats.counters, 'prefix_RRRY_' + case[4]), "prefix {} not counted ({})".format(case[4], case[0]))
        return pair

    def test_pairs(self):
        for case in prefix_cases:
            self.run_case(case)
        print("Ran {} prefix test cases.".format(len(cases)))

