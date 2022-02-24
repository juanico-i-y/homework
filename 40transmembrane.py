#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

import sys

#python3 40transmembrane.py ../MCB185-2022/Data/at_prots.fa

def kdcalc(aas):
	kdtot = 0
	for aa in aas:
		if aa == 'W': kdtot += -0.9
		if aa == 'C': kdtot += 2.5
		if aa == 'H': kdtot += -3.2
		if aa == 'M': kdtot += 1.9
		if aa == 'Y': kdtot += -1.3
		if aa == 'Q': kdtot += -3.5
		if aa == 'F': kdtot += 2.8
		if aa == 'N': kdtot += -3.5
		if aa == 'P': kdtot += -1.6
		if aa == 'T': kdtot += -0.7
		if aa == 'R': kdtot += -4.5
		if aa == 'I': kdtot += 4.5
		if aa == 'D': kdtot += -3.5
		if aa == 'G': kdtot += -0.4
		if aa == 'A': kdtot += 1.8
		if aa == 'K': kdtot += -3.9
		if aa == 'E': kdtot += -3.5
		if aa == 'V': kdtot += 4.2
		if aa == 'L': kdtot += 3.8
		if aa == 'S': kdtot += -0.8
	kd = kdtot / len(aas)
	return kd

def fattyhelix(pep, win, threshold):
	for i in range(0, len(pep) - win):
		seq = pep[i:i+win]
		if kdcalc(seq) > threshold and 'P' not in seq: 
			return True
	return False

#generate a list with a tuples that contains name and sequence
#for a nt sequence, flush on a line with a greater than sign
def readfasta(filename):
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			if line[0] == '>':
				if seq != '': yield((seqname, seq[:-1]))
				words = line.split() #splits by word
				seqname = words[0][1:]
				seq = ''
			else:
				seq += line.rstrip()
	
for name, prot in readfasta(sys.argv[1]):
	if fattyhelix(prot[0:30], 8, 2.5) == True and fattyhelix(prot[30:], 11, 2.0) == True:
		print(name)


"""
records = []
with open(sys.argv[1]) as fp:
	seq = ''
	seqname = ''
	for line in fp.readlines():
		if line[0] =! '>':
			if len(seq) > 0:
				records.append((seqname, seq))
				seq = ''
			words = line.split() #splits by word
			seqname = words[0][1:]
		else:
			seq += line.rstrip()
		if line[0] == '>': break
	records.append(seqname, seq)
	
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
