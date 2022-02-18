#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# Sorting the amino acids by frequency is optional

assert(len(sys.argv) == 2)

w = 0
c = 0
h = 0
m = 0
y = 0
q = 0
f = 0
n = 0
p = 0
t = 0
r = 0
i = 0
d = 0
g = 0
a = 0
k = 0
e = 0
v = 0
l = 0
s = 0

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line[0] != '>':
			for aa in line:
				if aa != '*': 
					if aa == 'W': w+=1
					if aa == 'C': c+=1
					if aa == 'H': h+=1
					if aa == 'M': m+=1
					if aa == 'Y': y+=1
					if aa == 'Q': q+=1
					if aa == 'F': f+=1
					if aa == 'N': n+=1
					if aa == 'P': p+=1
					if aa == 'T': t+=1
					if aa == 'R': r+=1
					if aa == 'I': i+=1
					if aa == 'D': d+=1
					if aa == 'G': g+=1
					if aa == 'A': a+=1
					if aa == 'K': k+=1
					if aa == 'E': e+=1
					if aa == 'V': v+=1
					if aa == 'L': l+=1
					if aa == 'S': s+=1
			
total = w + c + h + m + y + q + f + n + p + t + r + i + d + g + a + k + e + v + l + s
print('W', w, w/total)
print('C', c, c/total)
print('H', h, h/total)
print('M', m, m/total)
print('Y', y, y/total)
print('Q', q, q/total)
print('F', f, f/total)
print('N', n, n/total)
print('P', p, p/total)
print('T', t, t/total)
print('R', r, r/total)
print('I', i, i/total)
print('D', d, d/total)
print('G', g, g/total)
print('A', a, a/total)
print('K', k, k/total)
print('E', e, e/total)
print('V', v, v/total)
print('L', l, l/total)
print('S', s, s/total)

"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

