#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc = 0

for nt in range(len(dna)):
	if dna[nt] == 'G' or dna[nt] == 'C': gc += 1

print('%.2f' % (gc/len(dna))) #printf style
print('{:.2f}'.format(gc/len(dna))) #str.format method
print(f'{((gc/len(dna))):.2f}') #f string

#print in three formatting methods in 13text

#worked on this with Inglis and Kim!
"""
python3 21gc.py
0.42
0.42
0.42
"""
