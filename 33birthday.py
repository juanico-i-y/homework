#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

shared_birthdays = 0
calendar = [0]*365
people = 25
numtrials = 50

for trial in range(numtrials):
	for i in range(people):
		calendar[random.randint(0,364)] += 1
	for day in range(len(calendar)):
		if calendar[day] > 1:
			shared_birthdays += 1
			break

print(shared_birthdays/numtrials)


"""
python3 33birthday.py
0.571
"""

