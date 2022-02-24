#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

def readgb(filename):
	with open(sys.argv[1]) as fp:
		seq = ''
		for line in fp.readlines():
			match = re.search('.1 ([actg]){10}', line)
			if match:
				segments = line.split()
				seq += ''.join(segments[1:])
	seq = seq.rstrip()
	return seq

rpattern = sys.argv[2]
dnaseq = (readgb(sys.argv[1]))

cutregions = []
for site in re.finditer(rpattern, dnaseq):
	cutregions.append(site.span())

cutsites = [left[0] for left in cutregions]
print(cutsites)

for i in range(len(cutsites)):
	if i == 0: print(cutsites[0])
	elif i < len(cutsites):
		print(cutsites[i] - cutsites[i-1])
	else: print(len(dnaseq) - cutsites[i])

	
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
