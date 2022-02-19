import random
numtrials = 100000


for dc in range(1,21):
	ringwin = 0 #plus five to saving throws
	cloakwin = 0 #advantage
	
	for trial in range(numtrials):
		roll_1 = random.randint(1,20)
		roll_2 = random.randint(1,20)
		
		if roll_1 >= dc: 
			ringwin += 1
			cloakwin += 1
		else:
			if roll_2 >= dc: cloakwin += 1
			if roll_1 + 5 >= dc: ringwin += 1
	print(f' {dc} cloack save rate: {cloakwin/numtrials:.3f} ring save rate: {ringwin/numtrials:.3f}')

print('the ring is better')