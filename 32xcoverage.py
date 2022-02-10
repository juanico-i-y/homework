#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

#creating empty genome
genome = []
gensize = int(sys.argv[1])
genome = [0]*gensize

#extracting read number
readnum = int(sys.argv[2])

#extracting read length
readlength = int(sys.argv[3])

#NGS simulation
for i in range(readnum):
	start = random.randint(0, gensize - readlength)
	for bp in range(start, start + readlength):
		genome[bp] += 1

#calculating total reads, min, max
readtally = 0
gmin = genome[readlength]
gmax = genome[readlength]
for count in genome[readlength:-readlength]:
	readtally += count
	if count < gmin: gmin = count
	if count > gmax: gmax = count
	
print(f'{gmin} {gmax} {readtally/(gensize-(2*readlength)):.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
