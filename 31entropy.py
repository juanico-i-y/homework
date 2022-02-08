#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

sys.argv.pop(0)
probs = sys.argv

print(probs)

for x in range(len(probs)):
	probs[x] = int(probs[x])



#for p in probs
	#p * log(p)

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
