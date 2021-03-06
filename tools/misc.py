
def id_to_site():
    from spats_common import id_to_site
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/t7/"
    id_to_site(bp + "NOMASK_1.fq", bp + "RRRY.sam", bp + "YYYR.sam", 143)


def make_subset():
    from spats_common import make_subset
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    make_subset(bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq",
                bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq",
                bp + "t11/5s_missing.ids",
                bp + "t11/x")

def clean_sites():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    spats(bp + "5s/5S.fa",
          bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq",
          bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq",
          bp + "t11")

def d5s_writeback_run():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"

    from spats_shape_seq.db import PairDB
    pair_db = PairDB(bp + "dev_out/pairs.db")
    pair_db.add_targets_table(bp + "5s/5S.fa")

    from spats_shape_seq import Spats
    s = Spats()
    s.addTargets(bp + "5s/5S.fa")
    s.writeback_results = True
    s.result_set_name = "pure_python"
    s.process_pair_db(pair_db)

def d5s_run():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"

    #from spats_shape_seq.db import PairDB
    #pair_db = PairDB(bp + "dev_out/pairs.db")
    #if False:
    #    pair_db.add_targets_table(bp + "5s/5S.fa")
    #    pair_db.parse(bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq",
    #                  bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq")

    from spats_shape_seq import Spats
    from spats_shape_seq.partial import PartialFindProcessor
    s = Spats()
    #s.run._processor_class = PartialFindProcessor
    s.run.skip_database = True
    #s.run.writeback_results = True
    #s.run.resume_processing = True
    #s.run.result_set_name = "lookup"
    s.addTargets(bp + "5s/5S.fa")
    #s.process_pair_db(pair_db)
    s.process_pair_data(bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq",
                        bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq")
    s.compute_profiles()
    s.write_reactivities(bp + "dev_out/rx2.out")
    
def ligation_run():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/Shape_Seq_ligation/"
    from spats_shape_seq import Spats
    s = Spats()
    #s.config.debug = True
    #s.run.minimum_target_match_length = 10
    #s.run.num_workers = 1
    #from spats_shape_seq.partial import PartialFindProcessor
    #s.run._processor_class = PartialFindProcessor
    s.run.skip_database = True
    s.addTargets(bp + "panel_RNAs_complete.fa")
    s.process_pair_data(bp + "data/KEW1_S1_L001_R1_001.fastq",
                        bp + "data/KEW1_S1_L001_R2_001.fastq")

def cotrans_run():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"
    from spats_shape_seq import Spats
    s = Spats()
    #from spats_shape_seq.partial import PartialFindProcessor
    #s.run._processor_class = PartialFindProcessor
    s.run.skip_database = True
    #s.run.writeback_results = True
    #s.run.resume_processing = True
    #s.run.result_set_name = "lookup"
    s.addTargets(bp + "F_wt.fa")
    s.process_pair_data(bp + "data/EJS_6_F_10mM_NaF_Rep1_GCCAAT_R1.fastq",
                        bp + "data/EJS_6_F_10mM_NaF_Rep1_GCCAAT_R2.fastq")
    s.compute_profiles()
    s.write_reactivities(bp + "dev_out/rx.out")

def cotrans_test():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"
    from spats_shape_seq import Spats
    s = Spats()
    from spats_shape_seq.partial import PartialFindProcessor
    #s.run._processor_class = PartialFindProcessor
    s.addTargets(bp + "F_wt.fa")
    from spats_shape_seq.pair import Pair
    pair = Pair()
    pair.set_from_data('x', 'GAGCGTCCTTGGTGCCCGAGTCAGAAATAGACTCCT', 'TATCACTACTGGTAGGAGTCTATTTCTGACTCGGGC')
    s.process_pair(pair)
    print "{}: {}".format(pair.target.name, pair.site)

def run_5sq():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/5sq_dev/"
    spats(bp + "5S.fa",
          bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq", 
          bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq", 
          bp + "t4",
          show_sites = False)

def misc():
    if False:
        bp = "/Users/jbrink/mos/tasks/1RwIBa/refactor/spats/test/Read_Mapping/"
        spats(bp + "SRP_All_Stops.fa", bp + "SRP_All_Stops_R1.fq", bp + "SRP_All_Stops_R2.fq", bp + "t5")
    elif False:
        bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
        spats(bp + "5s/5S.fa",
              bp + "5s_sample/filtered_R1.fq",
              bp + "5s_sample/filtered_R2.fq",
              bp + "t11")
    else:
        bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/5sq_dev/"
        spats(bp + "5S.fa",
              bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq", 
              bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq", 
              bp + "t4")

def spats(target, r1, r2, out, show_sites = True):
    from spats_shape_seq import Spats, spats_config
    s = Spats()
    s.addTargets(target)
    s.addMasks("RRRY", "YYYR")
    if show_sites:
        spats_config.show_id_to_site = True
    s.process_pair_data(r1, r2)
    if not show_sites:
        s.compute_profiles()
        s.write_reactivities(out + "/rx.out")
              
def test_refactor():
    from spats_clean import Spats
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/5sq_dev/"
    out = bp + "t3/"
    s = Spats(bp + "5S.fa", out)
    s.setup()
    s.process_pair_data(bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq", 
                        bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq")
    s.compute_profiles()
    s.write_reactivities()
    import subprocess
    subprocess.check_call(["diff", bp + "t2/rx.out", out + "/rx.out"])
    print "Diff OK"

def make_id_case(arg = None, show = True, skip_site = False):
    import subprocess
    ident = arg or sys.argv[2]
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    R1 = subprocess.check_output([ "awk", "/" + ident + "/{getline; print; exit}", bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq" ]).strip('\n')
    R2 = subprocess.check_output([ "awk", "/" + ident + "/{getline; print; exit}", bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq" ]).strip('\n')
    if skip_site:
        site = None
    else:
        site = subprocess.check_output([ "awk", "/" + ident + "/{print $3; exit}", bp + "t11/5s-counts_sorted.out"]).strip('\n')
    case = "    [ '*{}', '{}', '{}', {} ],".format(ident, R1, R2, site or None)
    if show:
        print case
    return [ ident, R1, R2, site or None ]

def show_failure_types():
    from spats_clean import Spats, Pair, FastqRecord
    spats = Spats("test/5s/5s.fa", "test/5s")
    spats.setup()
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"

    with open(bp + "t11/x/filtered_R1.fq", 'rb') as r1_in:
        with open(bp + "t11/x/filtered_R2.fq", 'rb') as r2_in:
            r1_record = FastqRecord()
            r2_record = FastqRecord()
            pair = Pair()
            while True:
                r1_record.read(r1_in)
                if not r1_record.identifier:
                    break
                r2_record.read(r2_in)
                pair.set_from_records(r1_record, r2_record)

                spats.process_pair(pair)

                summary = "{} :: {}".format(pair.identifier, pair.site if pair.has_site else pair.failure)
                if pair.r1.match_errors:
                    summary += " R1!: {}".format(pair.r1.match_errors)
                if pair.r1.adapter_errors:
                    summary += " R1A!: {}, adapter_len={}".format(pair.r1.adapter_errors, pair.r1._rtrim)
                if pair.r2.match_errors:
                    summary += " R2!: {}".format(pair.r2.match_errors)
                if pair.r2.adapter_errors:
                    summary += " R2A!: {}, adapter_len={}".format(pair.r2.adapter_errors, pair.r2._rtrim - 4)
                print summary

def diag_case():
    from spats_shape_seq import Spats
    from spats_shape_seq.pair import Pair
    from spats_shape_seq.tests.test_mut import cases
    #from spats_shape_seq.tests.test_pairs import prefix_cases as cases
    from spats_shape_seq.diagram import diagram
    #spats_config.minimum_target_match_length = 8
    spats = Spats()
    #spats.addTargets("test/5s/5s.fa")
    spats.addTargets("test/mut/mut_single.fa")
    spats.run.debug = True
    spats.run.algorithm = "find_partial"
    spats.run.count_mutations = True
    #spats.run.mutations_require_quality_score = ord('.') - ord('!')
    spats.run.allowed_target_errors = 1
    spats.run.ignore_stops_with_mismatched_overlap = True
    spats.run.adapter_b = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"

    #spats.run.collapse_left_prefixes = True
    spats._case_errors = False
    def run_case(case):
        pair = Pair()
        pair.set_from_data(case[0], case[1], case[2])
        spats.process_pair(pair)
        print diagram(pair, spats.run)
        if case[3] != pair.site:
            spats._case_errors = True
            print "******* mismatch: {} != {}".format(case[3], pair.site)
    for case in cases:
        if case[0].startswith("*"):
            run_case(case)
    spats.run.debug = False
    if spats._case_errors:
        raise Exception("Case failed")

def test_compare_v102():
    from spats_shape_seq.v102 import compare_v102
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    compare_v102(bp + "s3",
                 bp + "5s/5S.fa",
                 'RRRY', 'YYYR',
                 bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq",
                 bp + "5s/data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq",
                 bp + "5S-2p1-18x/spats_out")

def test_compare_v102():
    from spats_shape_seq.v102 import compare_v102
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    compare_v102(bp + "s5",
                 bp + "datasets/Shape_Seq_ligation/panel_RNAs_complete.fa",
                 'RRRY', 'YYYR',
                 bp + "datasets/Shape_Seq_ligation/data/KEW1_S1_L001_R1_001.fastq",
                 bp + "datasets/Shape_Seq_ligation/data/KEW1_S1_L001_R2_001.fastq",
                 bp + "datasets/Shape_Seq_ligation/spats_out")

def diagram_v102():
    from spats_shape_seq.v102 import diagram_case
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/"
    diagram_case(bp + "s4/pairs.db",
                 14,
                 bp + "datasets/Shape_Seq_ligation/panel_RNAs_complete.fa",
                 'RRRY', 'YYYR')

def rc():
    from spats_shape_seq.util import reverse_complement
    print reverse_complement(sys.argv[2])

def makedb():
    db_path = sys.argv[2]
    targets_path = sys.argv[3]
    r1_path = sys.argv[4]
    r2_path = sys.argv[5]
    from spats_shape_seq.db import PairDB
    db = PairDB(db_path)
    db.show_progress_every = 200000
    db.load_and_index(targets_path, r1_path, r2_path)

def dbrun():
    db_path = sys.argv[2]
    run_name = sys.argv[3]
    from spats_shape_seq import Spats
    from spats_shape_seq.db import PairDB
    db = PairDB(db_path)
    s = Spats()
    s.run.writeback_results = True
    s.run.result_set_name = run_name
    #s.run.resume_processing = True
    s.process_pair_db(db)

def addv102():
    db_path = sys.argv[2]
    targets_path = sys.argv[3]
    out_path = sys.argv[4]
    from spats_shape_seq.db import PairDB
    db = PairDB(db_path)
    db.add_v102_comparison(targets_path, out_path)

def rdiff():
    rdiff_func(sys.argv[2], sys.argv[3], sys.argv[4])

def rdiff_func(db_path, rs1_name, rs2_name, diag_spats = None):
    from spats_shape_seq.db import PairDB
    from spats_shape_seq.diagram import diagram
    from spats_shape_seq.pair import Pair
    db = PairDB(db_path)
    n1 = db.num_results(rs1_name)
    n2 = db.num_results(rs2_name)
    print "{}: {} results  /  {}: {} results".format(rs1_name, n1, rs2_name, n2)
    if not n1 or not n2:
        print "** Abort."
        exit(1)
    print "Diffs:"
    ours_only = []
    theirs_only = []
    differences = []
    for r in db.differing_results(rs1_name, rs2_name):
        if r[4] == -1:
            assert(r[9] != -1)
            theirs_only.append(r)
        elif r[9] == -1:
            ours_only.append(r)
        else:
            differences.append(r)
    all_lists = [ ours_only, theirs_only, differences ]
    for l in all_lists:
        reasons = {}
        for r in l:
            key = r[7] or r[12] or "different values"
            assert(key)
            rlist = reasons.get(key)
            if not rlist:
                rlist = []
                reasons[key] = rlist
            rlist.append(r)
        for reason, rlist in reasons.iteritems():
            for r in rlist[:min(len(rlist), 10)]:
                print "  {}:{} s{}m{} ({}) -- {}:{} s{}m{} ({})   ([ '{}', '{}', '{}', {}, {}, [ {} ] ])".format(r[3] or 'x', r[4], r[5], r[6], r[7] or "OK",
                                                                                                                 r[8] or 'x', r[9], r[10], r[11], r[12] or "OK",
                                                                                                                 r[0], r[1], r[2], r[4], r[5], "" if -1 == r[6] else r[6] )
            if len(rlist) > 0:
                print "... {} total.".format(len(rlist))
            if diag_spats:
                pair = Pair()
                pair.set_from_data(str(r[0]), str(r[1]), str(r[2]))
                diag_spats.process_pair(pair)
                print diagram(pair, diag_spats.run)

    print "{} total diffs.".format(sum(map(len, all_lists)))

def test_tags():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/5sq_dev/"
    from spats_shape_seq import Spats
    s = Spats()
    from spats_shape_seq.tag import TagProcessor
    s.run._processor_class = TagProcessor

    #from spats_shape_seq.target import Targets
    #s.addTargets(bp + "5S.fa")
    s.addTarget("5s", "GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACCTGACCCCATGCCGAACTCAGAAGTGAAACGCCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGCGAGAGTAGGGAACTGCCAGGCATCTGACTCGGGCACCAAGGAC")
    #s.addTarget("rc(5s)", "GTCCTTGGTGCCCGAGTCAGATGCCTGGCAGTTCCCTACTCTCGCATGGGGAGACCCCACACTACCATCGGCGCTACGGCGTTTCACTTCTGAGTTCGGCATGGGGTCAGGTGGGACCACCGCGCTACGGCCGCCAGGCATCC")
    #s.addTarget("adapter_t", s.run.adapter_t)
    #s.addTarget("adapter_b", s.run.adapter_b)
    #s._targets._index_word_length = 8
    #s._targets._minimum_length = 8
    #s.addTarget("adapter_t_rc", reverse_complement(s.run.adapter_t))
    #s.addTarget("adapter_b_rc", reverse_complement(s.run.adapter_b))

    p = s._processor
    p.addTagTarget("5s", "GGATGCCTGGCGGCCGTAGCGCGGTGGTCCCACCTGACCCCATGCCGAACTCAGAAGTGAAACGCCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGCGAGAGTAGGGAACTGCCAGGCATCTGACTCGGGCACCAAGGAC")
    p.addTagTarget("5s_rc", "GTCCTTGGTGCCCGAGTCAGATGCCTGGCAGTTCCCTACTCTCGCATGGGGAGACCCCACACTACCATCGGCGCTACGGCGTTTCACTTCTGAGTTCGGCATGGGGTCAGGTGGGACCACCGCGCTACGGCCGCCAGGCATCC")
    from spats_shape_seq.util import reverse_complement
    p.addTagTarget("adapter_t_rc", reverse_complement(s.run.adapter_t))
    p.addTagTarget("adapter_b", s.run.adapter_b)

    from spats_shape_seq.pair import Pair
    cases = [
        [ "1101:20069:1063", "TTTAGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "TCCCACCTGACCCCATGCCGAACTCAGAAGTGAAA" ],
        [ "1101:11562:1050", "AAACGTCCTTGGTGCCCGAGTCAGATGCCTGGCAG", "CCACCTGACCCCATGCCGAACTCAGAAGTGAAACG" ],
        [ "21189", "TTTGGTCCTTGGTGCCCGAGTCAGAGATCGGAAGA", "CTGACTCGGGCACCAAGGACCAAAAGATCGGAAGA" ],
        [ "1101:12888:8140", "GGATGTCCTTGGTGCCCGAGTCAGATGCCAGATCG", "GGCATCTGACTCGGGCACCAAGGACATACAGATCG" ],
        [ "18333", "GAGTGTCCTTGGTGCCCGAGTCAGTGGTAGATCGG", "ACCACTGACTCGGGCACCAAGGACACTCAGATCGG" ],
    ]

    pair = Pair()
    for case in cases:
        pair.set_from_data(case[0], case[1], case[2])
        s.process_pair(pair)

        print pair.r1.original_seq
        print pair.r1.tags
        print pair.r2.original_seq
        print pair.r2.tags
        print "-----------------------------"

    #s.run.skip_database = True
    #s.run.writeback_results = True
    #s.run.resume_processing = True
    #s.run.result_set_name = "lookup"
    #s.process_pair_data(bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R1_001.fastq", 
    #                    bp + "data/17571-AD1AW-KEW11-5S-2p1-18x-23FEB15-GGCTAC_S10_L001_R2_001.fastq")


def tags():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"

    from spats_shape_seq.db import PairDB
    pair_db = PairDB(bp + "db/pairs.db")
    if True:
        print "Parsing to db..."
        pair_db.wipe()
        pair_db.add_targets_table(bp + "cotrans_single.fa")
        pair_db.parse(bp + "data/EJS_6_F_10mM_NaF_Rep1_GCCAAT_R1.fastq",
                      bp + "data/EJS_6_F_10mM_NaF_Rep1_GCCAAT_R2.fastq",
                      sample_size = 100000)

    from spats_shape_seq import Spats
    from spats_shape_seq.tag import TagProcessor
    from spats_shape_seq.util import reverse_complement
    s = Spats()
    s.run._processor_class = TagProcessor
    s.run.writeback_results = True
    s.run.result_set_name = "tags"
    s.run.num_workers = 1
    s.run.cotrans = True
    s.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
    s.loadTargets(pair_db)

    s.run.allow_indeterminate = True
    s.run.allowed_target_errors = 2
    s.run.allowed_adapter_errors = 2

    p = s._processor
    for target in pair_db.targets():
        p.addTagTarget(target[0], target[1])
        p.addTagTarget(target[0] + "_rc", reverse_complement(target[1]))
    p.addTagTarget("adapter_t_rc", reverse_complement(s.run.adapter_t))
    p.addTagTarget("adapter_b", s.run.adapter_b)
    if s.run.cotrans:
        p.addTagTarget("linker_cotrans", s.run.cotrans_linker)
        p.addTagTarget("linker_cotrans_rc", reverse_complement(s.run.cotrans_linker))

    s.process_pair_db(pair_db)
    rsid = pair_db.result_set_id_for_name(s.run.result_set_name)
    pair_db.count_tags(rsid)
    print pair_db.tag_counts(rsid)


def tquery():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"

    from spats_shape_seq.db import PairDB
    pair_db = PairDB(bp + "db/pairs.db")
    print pair_db.results_matching(1, [ "linker_cotrans", "adapter" ], [ "match" ])

def tag_test():
    from spats_shape_seq import Spats
    s = Spats()
    s.run.cotrans = True
    s.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
    s.run.algorithm = "find_partial"

    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"
    s.addTargets(bp + "cotrans_single.fa")

    from spats_shape_seq.pair import Pair
    pair = Pair()
    import cjb.util
    d = cjb.util.jsonAtPath("/tmp/spats_test.json")
    pair.set_from_data(str(d['id']), str(d['r1']), str(d['r2']))
    print "{}\n{} / {}".format(pair.identifier, pair.r1.original_seq, pair.r2.original_seq)
    s.process_pair(pair)
    if pair.has_site:
        print "{}: {} / {}".format(pair.target.name, pair.site, pair.right)
    else:
        print "FAIL: {}".format(pair.failure)

def cotrans_debug():
    from spats_shape_seq import Spats
    s = Spats()
    s.run.cotrans = True
    #s.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
    #s.run.algorithm = "find_partial"
    #s.run._p_v102_compat = True
    s.run.minimum_target_match_length = 10
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/"
    s.addTargets(bp + "cotrans_single.fa")

    from spats_shape_seq.pair import Pair
    pair = Pair()

    import cjb.util
    d = cjb.util.jsonAtPath("/tmp/spats_test.json")
    pair.set_from_data(str(d['id']), str(d['r1']), str(d['r2']))
    #c = ['683779', 'TCCGGTCCTTGGTGCCCGAGTCAGAAAAAAATAGAA', 'TCTATTTTTTTCTGACTCGGGCACCAAGGACCGGAA', 82, 71]
    #c = [ "1116:19486:8968", "TCCGGTCCTTGGTGCCCGAGTCAGTCCTTCCTCCTA", "GAGTCTATTTTTTTAGGAGGAAGGACTGACTCGGGC", 93, 68 ]
    #c = [ "301028", "AAGTGTCCTTGGTGCCCGAGTCAGAGATAGATCGGA", "ATCTCTGACTCGGGCACCAAGGACACTTAGATCGGA", 96, 92 ]
    #c = [ "31631284", "TTCAGTCCTTGGTGCCCGAGTCAGAGATAGATCGGA", "ATCTCTGACTCGGGCACCAATGACCGGAAGATCGGA", 96, 92 ]
    #c = [ "7232", "AGGTGTCCTTGGTGCCCGAGTCAGTAGCTAAGAAAT", "TTATAGGCGATGGAGTTCGCCATAAACGCTGCTTAG", -1, -1 ]
    #c = [ "16845404", "AAATGTCCTTGGTGCCCGAGTCAGACTGGTAGGAGT", "TCTTATAGGCGATGGAGTTCGCCATAAACGCTGCTT", -1, -1 ]
    #c = [ "24102328", "AAGCGTCCTTGGTGCCCGAGTCAGGAGTCATAGATC", "ATGACTCCTGACTCGGGCACCAAGGACGCTTAGATC", 46, 39 ]
    #c = [ "51216106", "GGGTGTCCTTGGTGCCCGAGTCAGATTAGCTAAGCA", "AGCTAATCTGACTCGGGCACCAAGGACGCTGCTTAG", 41, 34 ]
    c = [ "1116:19486:8968", "TCCGGTCCTTGGTGCCCGAGTCAGTCCTTCCTCCTA", "GAGTCTATTTTTTTAGGAGGAAGGACTGACTCGGGC", 93, 68 ]
    #c = [ "41823514", "GAATGTCCTTGGTGCCCGAGTCAGAACTCCAAGATC", "TGGAGTTCTGACTCGGGCACCAAGGACATTCAGATC", -1, -1 ]
    #c = [ "180", "AAGCTGTCCTTGGTGCCCGAGTCAGGAAAAGTTCTT", "TTTTTTTAGGAGGAAGGATCTATGAGCAAAGGAGAA", 120, 75 ]
    #c = [ "67219", "GAGTGTCCTTGGTGCCCGAGTCAGTCGACAACTCCA", "TTATAGGCGATGGAGTTCGCCATAAACGCTGCTTAG", 134, 0 ]
    #c = [ "58726", "GGATGTCCTTGGTGCCCGAGTCAGCCTTAGATCGGA", "AAGGCTGACTCGGGCACCAAGGACATCCAGATCGGA", None, None ]
    #c = [ "188425", "GGACGTCCTTGGTGCCCGAGTCAGTATAGATCGGAA", "ATACTGACTCGGGCACCAAGGACTTCCAGATCGGAA", 24, 21 ]
    #c = [ "jjb_L21", "GGACGTCCTTGGTGCCCGAGTCAGGGCGAACTAGAT", "AGTTCGCCCTGACTCGGGCACCAAGGACGTCCAGAT", 21, 13 ]
    #c = [ "jjb_L20", "GGACGTCCTTGGTGCCCGAGTCAGGCGAACTCAGAT", "GAGTTCGCCTGACTCGGGCACCAAGGACGTCCAGAT", 20, 12 ]
    #c = [ "jjb_L19", "GGACGTCCTTGGTGCCCGAGTCAGCGAACTCCAGAT", "GGAGTTCGCTGACTCGGGCACCAAGGACGTCCAGAT", None, None ]
    #c = [ "406149", "AGGTGTCCTTGGTGCCCGAGTCAGGACAACTCCAGT", "TTATAGGCGATGGAGTTCGCCATAAACGCTGCTTAG", 132, 0 ]
    #c = [ "89185", "TCCAGTCCTTGGTGCCCGAGTCAGCTAAGCAGCGTT", "AATGACTCCTACCAGTATCACTACTGGTAGGAGTCT", 36, 38 ]
    #c = [ "3185000", "GAACGTCCTTGGTGCCCGAGTCAGGTTTATGGCGAA", "TCGCCATAAACCTGACTCGGGCACCAAGGACGTTCC", -1, -1 ]
    #c =     [ "jjb_3185000'", "GAACGTCCTTGGTGCCCGAGTCAGGTTTATGGCGAA", "TCGCCATAAACCTGACTCGGGCACCAAGGACGTTCA", None, None ]
    #c = ['1', 'TCTGAGATCGGAAGAGCACACGTCTGAACTCCAGT', 'CAGAAGATCGGAAGAGCGTCGTGTAGGGAAAGAGT', None, None]
    #c = ['24941', 'TCCAGTCCTTGGTGCCCGAGTCAGAGACTCCTACCA', 'TATAGGCGATGGAGTTCGCCATAAACGCTGCTTAGC', -1, -1]
    c = ['jjbn', 'TTTGGTCCTTGGTGCCCGAGTCAGTAAAAAAATAGA', 'TCTATTTTTTTACTGACTCGGGCACCAAGGACCAAA', 83, 71 ]
    pair.set_from_data(c[0], c[1], c[2])
    print "{}\n{} / {}".format(pair.identifier, pair.r1.original_seq, pair.r2.original_seq)
    s.process_pair(pair)
    if pair.has_site:
        print "{}: {} / {}".format(pair.target.name, pair.site, pair.end)
    else:
        print "FAIL: {}".format(pair.failure)

def prof_run():
    from spats_shape_seq import Spats
    spats = Spats()
    #spats.run.cotrans = True
    #spats.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
    #spats.run.writeback_results = False
    spats.run._process_all_pairs = True
    spats.run.skip_database = True
    spats.run.algorithm = "lookup"
    spats.run.count_mutations = True
    spats.run.num_workers = 1

    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/pdc_muts/PDC_tweaked/PDC_09_001_6/"
    spats.addTargets(bp + "target.fa")
    spats.process_pair_data(bp + "2k_R1.fastq",
                            bp + "2k_R2.fastq")
    exit(0)

def make_test_dataset():
    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/datasets/cotrans/data/"
    from spats_shape_seq import Spats
    from spats_shape_seq.db import PairDB
    pair_db = PairDB(bp + "ds.spats")
    pair_db.add_targets_table(bp + "../cotrans_single.fa")
    pair_db.parse(bp + "med_R1.fq", bp + "med_R2.fq")
    s = Spats(cotrans = True)
    s.run.num_workers = 1
    s.run.writeback_results = True
    s.run._process_all_pairs = True
    s.run.algorithm = "find_partial"
    s.run.result_set_name = "test_validation"
    s.process_pair_db(pair_db)
    pair_db.store_run(s.run)
    pair_db.store_counters('spats', s.counters)

def tabif():
    from spats_shape_seq.parse import abif_parse
    fields = [ 'DATA2', 'DATA3', 'DATA105' ]
    data = abif_parse("/Users/jbrink/mos/tasks/1RwIBa/tmp/abif/abifpy/PDC.ab1", fields)
    def m1(data):
        return sum([(i + 1) * data[i] for i in range(len(data))])/sum(data)
    for i in range(len(fields)):
        print "m1[{}] = {}".format(i, m1(data[i]))

def tnb():
    from spats_shape_seq.nbutil import Notebook
    nb = Notebook('test_out.ipynb')
    if nb.is_empty():
        nb.add_code_cell("a = [1,2,3,4]*2\nb = [x for x in reversed(a)]\nb")
    nb.save(nb.path)

def tm():
    from spats_shape_seq.matrix import matrix_html
    print matrix_html(20, 131, None)

def tmut():
    from spats_shape_seq import Spats
    from spats_shape_seq.db import PairDB
    from spats_shape_seq.diagram import diagram

    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/mutsl/"

    pair_db = PairDB(bp + "ds_cmp.spats")
    if True:
        print "Parsing to db..."
        pair_db.wipe()
        pair_db.add_targets_table(bp + "mut_single.fa")
        fq_name = "mut2"
        pair_db.parse(bp + fq_name + "_R1.fastq", bp + fq_name + "_R2.fastq")

    spatss = []
    for alg in [ "find_partial", "lookup" ]:
        spats = Spats(cotrans = False)
        spats.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
        spats.run.count_mutations = True
        spats.run.algorithm = alg
        spats.run.allowed_target_errors = 1
        spats.run.adapter_b = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"
        spats.run._process_all_pairs = True
        spats.run.writeback_results = True
        spats.run.num_workers = 1
        spats.run.result_set_name = "mut_" + alg

        spats.process_pair_db(pair_db)
        pair_db.store_run(spats.run)
        pair_db.store_counters(spats.run.result_set_name, spats.counters)
        spatss.append(spats)

    rdiff_func(bp + "ds_cmp.spats", "mut_find_partial", "mut_lookup", diag_spats = spatss[0])

    #for key, value in spats.counters._registered.iteritems():
    #    if ":M" in key:
    #        print "{}: {}".format(key, value)


def tmut_case():
    from spats_shape_seq import Spats
    from spats_shape_seq.db import PairDB
    from spats_shape_seq.diagram import diagram

    bp = "/Users/jbrink/mos/tasks/1RwIBa/tmp/mutsl/"

    spats = Spats(cotrans = False)
    spats.run.cotrans_linker = 'CTGACTCGGGCACCAAGGAC'
    spats.run.count_mutations = True
    spats.run.algorithm = "find_partial"
    spats.run.allowed_target_errors = 1
    spats.run.adapter_b = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"
    spats.run._process_all_pairs = True
    spats.run.writeback_results = True
    spats.run.num_workers = 1
    spats.run.result_set_name = "mut"
    spats.addTargets(bp + "mut_single.fa")

    from spats_shape_seq.pair import Pair
    pair = Pair()

    #c = [ 'GAATGTCCTTGGTGCCCGAGTCAGTCCTTGGTGCCCGAGTCAGTCCTTGGTTCCCGAGTCACTCCTTTGTTCCCC', 'AGGACTGACTCGGGCACCAAGGACTTTCTCGTTCACCTATTTCTTTCTCTTCCCCCTTTTTCTTTCTCTTTCTCC' ]
    #c = [ 'GAGCGTCCTTGGTGCCCGAGTCAGATGCCGACCCGGGTGGGGGCCCTGCCAGCTACATCCCGGCACACGCGTCAT', 'TAGGTCAGGTCCGGAAGGAAGCAGCCAAGGCAGATGACGCGTGTGCCGGGATGTAGCTGGCAGGGCCCCCACCCG' ]
    #c = [ 'GAATGTCCTTGGTGCCCGAGTCAGGACACGCGTCATCTGCCTTGGCTGCTTCCTTCCGGACCTGACCTGGTAAAC', 'ATCGGGGGCTCTGTTGGTTCCCCCGCAACGCTACTCTGTTTACCAGGTCAGGTCCGGAAGGAAGCAGCCAAGTCA' ]
    #c = [ 'AGGCGTCCTTGGTGCCCGAGTCAGCCTTGGCTGCTTCCTTCCGGACCTGACCTGGTAAACAGAGTAGCGTTGCGG', 'ATCGGGGGCTCTGTTGGTTCCCCCGCAACGCTACTCTGTTTACCAGGTCAGGTCCGGAAGGAAGCAGCCAAGTCT' ]
    #c = [ 'TTCAGTCCTTGGTGCCCGAGTCAGCCAGCTACATCCCGGCACACGCGTCATCTGCCTTGGCTGCTTCCTTCCGGA', 'AGGTCAGATCCGGAAGGAAGCAGCCAAGGCAGATGACGCGTGTGCCGGGATGTAGCTGGCTGACTCGGGCACCAA' ]
    #c = [ 'AAATGTCCTTGGTGCCCGAGTCAGATCTGCCTTAAGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGA', 'TAAGGCAGATCTGACTCGGGCACCAAGGACATTTAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCG' ]
    #c = [ 'CTCAGTCCTTGGTGCCCGAGTCAGTGAGCTAGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTC', 'AGCTCACTGACTCGGGCACCAAGGACTGAGAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGG' ]
    #c = [ 'AAGCGTCCTTGGTGCCCGAGTCAGTGGAGGTAGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCT', 'ACCTCCACTGACTCGGGCACCAAGGACGCTTAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTG' ]
    #c = [ 'TCCGGTCCTTGGTGCCCGAGTCAGATGTAGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGT', 'ACATCTGACTCGGGCACCAAGGACCGGAAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTC' ]
    #c = [ 'TTTAAGTCCTTGGTGCCCGAGTCAGGTCATCTGCCTTGGCTGCTTCCTTCCGGACCTGACCTGGTAAACAGAGTA', 'TACTCTGTTTACCAGGTCAGGTCCGGAAGGAAGCAGCCAAGGCAGATGACCTGACTCGGGCACCAAGGACTTAAA' ]
    #c = [ 'TTCACAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCATTAACCTCCTGAATCACTAT', 'GGACAAGCAATGCTTACCTTGATGTTGAACTTTTGAATAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGA' ]
    #c = [ 'AGATCAACAAGAATTAGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCATTAACCTCCTGAATCACTAT', 'ACAAGCAATGCTTGCCTTGATGTTGAACTTTTGAATAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGAAC' ]
    #c = [ 'AAATCAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCATTAACCTCCTGAATCACTAT', 'AATAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGATT' ]
    #c = [ 'TCCGCAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCATTAACCTCCTGAATCACTAT', 'ATAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGCGGA' ]
    #c = [ 'TCCACAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCATTTGCTCATCATTAACCTCCTGAATCACTAT', 'GGACAAGCAATGCTTGCCTTGATGTTGAACTTTTGAATAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGA' ]
    #c = [ 'GGGTCAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCATTTAGATCGGAAGAGCACAC', 'AAATGATGAGCAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGACCCAGATCGGAAGAGCGTCG' ]
    c = [ 'GAACCAACAAGAATTGGGACAACTCCAGTGAAAGGTTCTTCTCCTTTGCTCATCATTAACCTCCTGAAGATCGGA', 'TCAGGAGGTTAATGATGAGCAAAGGAGAAGAACCTTTCACTGGAGTTGTCCCAATTCTTGTTGGTTCAGATCGGA' ]
    #c = [ 'CCTACAACAAGAATTGGGACAACTCCAGTGAGAAGTTCTTCTCCTTTGCTCATCATTAAGATCGGAAGAGCACAC', 'TAATGATGAGCAAAGGAGAAGAACTTCTCACTGGAGTTGTCCCAATTCTTGTTGTAGGAGATCGGAAGAGCGTCG' ]
    #c = [ 'CTTGCAACAAGAATTGGGACAACTCCAGTGAAAAGTTCTTCTCCTTTGCTCATCTTTAACCTCCTGAATCACTAA', 'TAGTGATTCAGGAGGTTAATGATGAGCAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGCAAGA' ]
    pair.set_from_data('x', c[0], c[1])
    spats.process_pair(pair)
    print diagram(pair, spats.run)
    if pair.has_site:
        print "{}: {} / {} {}".format(pair.target.name, pair.site, pair.end, pair.mutations)
    else:
        print "FAIL: {}".format(pair.failure)
    
def indels_run():
    from spats_shape_seq import Spats
    s = Spats()
    s.run.algorithm = True
    s.run.count_indels = True
    s.run.count_mutations = True
    s.run.allowed_target_errors = 8
    s.collapse_left_prefixes = True
    s.run.ignore_stops_with_mismatched_overlap = True
    s.run.allow_negative_values = True
    s.mutations_require_quality_score = 30
    bp = "/Users/steve/mos/tasks/oughxX/code"
    s.addTargets(bp + "/test/hairpin/hairpinA_circ.fa")
    rp = bp + "/TESTING/cmp_muts_favored/steve_test"
    s.process_pair_data(rp + "/R1_match_failures.fastq",
                        rp + "/R2_match_failures.fastq")
    exit(0)

def align_pairs():
    from spats_shape_seq.pair import Pair
    from spats_shape_seq.target import Targets
    from spats_shape_seq.util import reverse_complement, AlignmentParams
    from spats_shape_seq.mask import Mask, match_mask_optimized, base_similarity_ind

    target_seq = "GGACCCGATGCCGGACGAAAGTCCGCGCATCAACTATGCCTCTACCTGCTTCGGCCGATAAAGCCGACGATAATACTCCCAAAGCCC"  # HairpinC_SS2
    r1_seq = "GGGTGAGCGTGCTTTGGGAGTATTATCGTCGGCTTTATCGGCCGAAGCAGGTAGTGCATAGTTGATGCTCGGACTTTCG"
    r2_seq = "GGACCCGATGCCGGACGAAAGTCCGAGCATCAACTATGCCCTACCTGCTTCGGCCGATAAAGCCAAAAGACGATAAT"

    pair = Pair()
    pair.set_from_data("TEST_PAIR", r1_seq, r2_seq)
    targets = Targets()
    targets.minimum_match_length = 10
    targets.addTarget("TEST_TARGET", target_seq, 0)
    targets.index()

    mask = match_mask_optimized(pair.r1.original_seq)
    assert(mask)
    pair.set_mask(Mask(mask))
    target = pair.r1.find_in_targets(targets)
    pair.target = pair.r2.find_in_targets(targets, force_target = target)
    assert(pair.matched)

    masklen = pair.mask.length()
    adapter_t = "AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT"
    r2suffix = reverse_complement(pair.r1.original_seq[:masklen]) + reverse_complement(adapter_t)
    simfn = lambda nt1, nt2: base_similarity_ind(nt1, nt2, 3, 2, 1.5)
    ap = AlignmentParams(simfn, 5, 1)

    pair.r2.align_with_target(pair.target, ap, r2suffix)
    r2_adapter_trim = max(0, pair.r2.match_index + pair.r2.match_len - pair.target.n)
    r1_adapter_trim = pair.r1.seq_len - (pair.target.n - pair.r2.match_index)
    if r1_adapter_trim > 0:
        pair.r1.rtrim += r1_adapter_trim
        pair.r1.match_start -= r1_adapter_trim
    pair.r1.align_with_target(pair.target, ap)

    exit(0)



if __name__ == "__main__":
    import sys
    globals()[sys.argv[1]]()
