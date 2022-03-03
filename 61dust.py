#!/usr/bin/env python3
# 61dust.py

import argparse
import math
from mcb185 import *
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file (FASTA)
#   window size
#   entropy threshold- calc with Shannon Entropy Calculator
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

#parse for fasta, window size, entropy threshold, output fasta line length, lowercase or N-based masking
parser = argparse.ArgumentParser(description='Scan FASTA for N-based masking based on entropy threshold.')

parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required fasta file')
parser.add_argument('--winsize', required=True, type=int,
	metavar='<int>', help='required integer argument')
parser.add_argument('--ethreshold', required=False, type=float, default=0.70,
	metavar='<float>', help='optional floating point argument [%(default).3f]')
parser.add_argument('--linelength', required=False, type=int, default=50,
	metavar='<int>', help='optional integer argument for fasta line length [%(default)i]')
parser.add_argument('--lowercase', action='store_true',
	help='change to lowercase masking. Default is N-masking.')
arg = parser.parse_args()

#selecting a sequence rewriter function: lowercase masking or N-based masking
if arg.lowercase: rewriter = l_entropy_seq_rewriter
else: rewriter = n_entropy_seq_rewriter

#writing masked fasta sequence
for name, seq in read_fasta(arg.fasta):
	rewrite = rewriter(seq, arg.ethreshold, arg.winsize)
	print(f'>{name}')
	for i in range(0, len(rewrite), arg.linelength):
		print(rewrite[i:i+arg.linelength])