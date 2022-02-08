#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

sys.argv.pop(0)
nlist = sys.argv

for x in range(len(nlist)):
	nlist[x] = int(nlist[x])
nlist.sort()

count = 0
total = 0
xmew = 0

for num in nlist:
	count += 1
	total += num

mean = total/len(nlist)

#std dev calculation
totdiff = 0
diffsqr = 0
for num in nlist:
	diff = num - mean
	diffsqr = diff**2
	totdiff += diffsqr

std = math.sqrt(totdiff/count)

#median calculation
if (len(nlist)/2) % 1 == 0: #even number of numbers
	left = int(len(nlist)/2)
	right = left + 1
	medsum = left + right
	median = medsum / 2
	
else: #odd number of numbers
	a = int(len(nlist)/2 - .5)
	median = nlist[a]

print('Count:', count)
print('Minimum:', nlist[0])
print('Maximum:', nlist[len(nlist)-1])
print('Mean:', mean)
print('Std. dev', std)
print('Median:', median)

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
