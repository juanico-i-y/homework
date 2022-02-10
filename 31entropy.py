#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi)), base 2
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

#entropy means randomness. Closer outcome is to 1, then less entropy
import math
import sys

probs = []
for i in range (1, len(sys.argv)): probs.append(float(sys.argv[i]))

#to check if probabilities add to 1
totprob = 0
for num in probs:
	totprob += num
if (totprob - 1.0) > .00001:
	print('probabilities do not add to 1')
	sys.exit()

entropy = 0
for num in probs:
	entropy += (-num*math.log2(num))
print(f'{entropy:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
