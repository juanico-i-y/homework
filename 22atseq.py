#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

dna = ''

for i in range(30):
	if random.random()>0.6:
		if random.random()>0.5:
			dna+='G'
		else: dna+='C'
	else:
		if random.random()>0.5:
			dna+='A'
		else: dna+='T'

at = 0
for i in range(len(dna)):
	if dna[i] == 'A': at += 1
	if dna[i] == 'T': at += 1
atpercent = at/len(dna)

print(len(dna), atpercent, dna)
	
	
# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

#create a variable for DNA
#every time loop ocurs, add AT or CG

#worked on this with Inglis and Kim!
"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
