#99final_project.py ../MCB185/Data/Dovetail_mRNA

import random
from mcb185 import*
import sys
import re

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

nlspat = {
	'MP classic' : 'K[KR][^KR][KR]',
	'MP SV-40': 'PKKKRKV',
	'MP VACM-1/CUL5' : '(?=.{5}$)(?=.{3}[KR])P',
	'MP CXCR4' : '[KR]P[KR][KR]',
	'BP' : '(?=.{15,17}$)[RK][^KRP]*[P][^KRP]*KR[^KR]K'
}

def translate(seq):
	protein = ''
	for i in range(0, len(seq)-2, 3):
		codon = seq[i:i+3]
		if codon in gcode: protein += gcode[codon]
		else: protein += 'X'
	return protein

#tranlsate mRNA, search proteins for an nls, record nls and number times found
totalseq = 0
global_patfound = {} #all patterns found in Hydra protein list
patfound = {} #will contain each protein and nls found in it

for name, seq in read_fasta(sys.argv[1]):
	prot = translate(seq)
	totalseq += 1
	global_matchcount = 0
	matchlist = []
	
	for patname, pat in nlspat.items():
		match = re.search(pat, prot)
		if match:
			global_matchcount += 1
			matchlist.append(patname)
			if patname not in global_patfound:
				global_patfound[patname] = 1
			else:
				global_patfound[patname] += 1
		patfound[name] = matchlist


print(f'{totalseq} total protein sequences')
print(f'These matches were found globally: {global_patfound} \n')

print('expected nls')
print('Jun,', patfound['g23720.t1'])
print('Fos,', patfound['g1450.t1'])
print('cr3l,', patfound['g32585.t1'])
print('creb,', patfound['g16491.t1'])

print('\n')
print('not expecting nls')
print('axin,', patfound['g14938.t1'])
print('wnt3,', patfound['g28065.t1'])
print('wnt9/10c,', patfound['g33373.t1'])
print('dishevelled,', patfound['g29781.t1'])
