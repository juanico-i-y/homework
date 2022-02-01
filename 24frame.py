#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'
frame=0

for i in range(len(dna)):
	print(i, end = ' ')
	if frame == 0:
		frame += 1 
		print(0, end = ' ')
	elif frame == 1:
		frame += 1
		print (1, end = ' ')
	elif frame == 2:
		frame += -2
		print (2, end = ' ')
	print(dna[i])


for i in range(len(dna)):
	print(i, end = ' ')
	for b in range(2):
		if (



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
