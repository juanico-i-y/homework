# mcb185.py

import sys
import gzip
import math

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# def other functions...

def entropy_calc(seq):
	shannon_list = []
	
	a_fraction = seq.count('A')/len(seq)
	c_fraction = seq.count('C')/len(seq)
	t_fraction = seq.count('T')/len(seq)
	g_fraction = seq.count('G')/len(seq)
	
	if a_fraction > 0: shannon_list.append(a_fraction)
	if c_fraction > 0: shannon_list.append(c_fraction)
	if t_fraction > 0: shannon_list.append(t_fraction)
	if g_fraction > 0: shannon_list.append(g_fraction)
	
	entropy = 0
	for fraction in shannon_list:
			entropy += (-fraction*math.log2(fraction))
	return entropy

#N-based masking
def n_entropy_seq_rewriter(seq, threshold, w):
	rewrite_list=[]
	rewrite_list[:0] = seq

	for i in range(0, len(seq) - w+1):
		window = seq[i:i+w]
		if entropy_calc(window) < threshold:
			for nt in range(w):
				rewrite_list[i+nt] = 'N'
	rewrite = "".join(rewrite_list)
	return rewrite

#lowercase masking
def l_entropy_seq_rewriter(seq, threshold, w):
	rewrite_list=[]
	rewrite_list[:0] = seq
	
	for i in range(0, len(seq) - w+1):
		window = seq[i:i+w]
		if entropy_calc(window) < threshold:
			for nt in range(w):
				if seq[nt] == 'A': rewrite_list[nt+i] = 'a'
				if seq[nt] == 'C': rewrite_list[nt+i] = 'c'
				if seq[nt] == 'T': rewrite_list[nt+i] = 't'
				if seq[nt] == 'G': rewrite_list[nt+i] = 'g'	
	rewrite = "".join(rewrite_list)
	return rewrite
