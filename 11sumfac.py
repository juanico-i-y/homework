#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

# your code goes here

n = 5
runsum=0
runmult=1
for n in range (1,n+1):
	runsum+=n
	runmult*=n
print(n,runsum,runmult)


"""
#expected output
python3 11sumfac.py
5 15 120
"""
