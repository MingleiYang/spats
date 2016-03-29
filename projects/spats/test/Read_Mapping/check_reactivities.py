#!/usr/bin/env python

"""
Summarizes resulting reactivities.out of spats based on expected results. Part of Read_Mapping tests.
Usage: python check_reactivities.py --input <> --output <> --permutation <> --adapter <> --sequence <>
Options: 
 --input	reactivities.out file from spats
 --output	File to output result summary
 --permutation	Choice of all 16 binary permutations of length 4. This represents the pattern of reads mapped we expect for every 2 reads in their + and - channel. Limited to 0-15.
 --adapter	Adapter sequence
 --sequence	Sequence of RNA target
Version: 0.1
Date: March 29, 2016
Author: Angela M Yu
Copyright (c) 2016 Lucks Laboratory - all rights reserved.
"""

from itertools import product, cycle
import getopt
import sys

def getopts(short_arg_string, long_arg_list):
    """
    Returns a dictionary of command line arguments as defined by short_arg_string and long_arg_list
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:],short_arg_string,long_arg_list)
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    return dict(opts)

opts = getopts("", ["input=", "output=", "permutation=", "adapter=", "sequence="])
spats_reactivities_out = opts["--input"]
output = opts["--output"]
permutation = int(opts["--permutation"])
adapter_len = len(opts["--adapter"])
sequence_len = len(opts["--sequence"])

all_permutations = [seq for seq in product([0,1], repeat=4)]
permutation_cycle = cycle(all_permutations[permutation])
print "Checking permutation %s: %s..."%(permutation, all_permutations[permutation])

reads = []
with open(spats_reactivities_out, "r") as f:
    header = f.readline()
    for line in f:
        fields = line.split("\t")
        reads += [int(fields[4]), int(fields[5])]

correct = sum([1 if a[0] == a[1] else 0 for a in zip(permutation_cycle, reads[:2*(sequence_len+1)])])
correct += sum([1 if a == 0 else 0 for a in reads[2*(sequence_len+1):]])
incorrect = len(reads) - correct
exp_read_lines = 2 * (sequence_len + adapter_len + 1)

if correct == len(reads) and len(reads) == exp_read_lines:
    result = "Permutation %s %s: OK - %s read positions out of %s expected, %s correct\n"%(permutation, all_permutations[permutation], len(reads), exp_read_lines, correct)
else:
    result = "Permutation %s %s: FAILED - %s read positions out of %s expected, %s incorrect, %s correct\n"%(permutation, all_permutations[permutation], len(reads), exp_read_lines, incorrect, correct)

print result
with open(output, "a") as f:
    f.write(result)
