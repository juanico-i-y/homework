#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

for i in range(0,len(dna))
	print(i+1)
	if (i+1) % 2 == 0: print(2)
	elif (i+1) % 3 == 0: print(3)
	else: print(3)
	print(dna[i])

"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
