import random

numtrials = 100000

revive = 0
stabilize = 0
die = 0

for trials in range(numtrials):
	success = 0
	fail = 0
	lucky = 0

	while success < 3 and fail < 3 and lucky == 0:
		roll = random.randint(1,20)
		
		if roll == 20: lucky += 1
		elif roll >= 10: success += 1
		elif roll < 10: fail += 1
		
		if lucky == 1:
			revive += 1
		elif success == 3:
			stabilize += 1
		elif fail == 3:
			die += 1

print(f'revive {revive/numtrials:.3f} stabilize {stabilize/numtrials:.3f} die {die/numtrials:.3f}')
