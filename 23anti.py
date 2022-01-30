#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
revdna = dna[::-1]
revcomp = ''

for i in range(len(revdna)):
	if revdna[i] == 'A': revcomp += 'T'
	elif revdna[i] == 'T': revcomp += 'A'
	elif revdna[i] == 'G': revcomp += 'C'
	else: revcomp += 'G'
print(revcomp)
	
#worked with Inglis, Kim, Majken

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
