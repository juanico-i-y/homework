import random

numtrials = 1000000
eadmg = 0
ndmg = 0

for trial in range(numtrials):
	roll = random.randint(1,10)
	
	if roll == 1:
		ndmg += 1
		eadmg += 2
	else:
		ndmg += roll
		eadmg += roll

print(f' difference is {((eadmg-ndmg)/numtrials):.3f}')