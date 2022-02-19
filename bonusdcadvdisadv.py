import random

trials = 100000

print('dc', 'norm', 'adv', '  dis')

for dc in range(1,21):
	norm = 0
	dis = 0
	adv = 0
	for i in range(trials):
		roll_1 = random.randint(1,20)
		roll_2 = random.randint(1,20)
	
		if roll_1 >= dc: 
			norm += 1
			adv += 1
			if roll_2 >= dc: dis += 1
		else:
			if roll_2 >= dc: adv += 1
	print(f'{dc} {norm/trials:.3f} {adv/trials:.3f} {dis/trials:.3f}')
