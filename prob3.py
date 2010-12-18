#! /usr/local/bin/python

v = 600851475143
maxfactor = 1
found = 1

while ((v != 1) and (found)):
	factor = 2
	while (((factor*factor) < v) and ((v % factor) != 0)):
		factor = factor + 1

	found = 0
	if ((v % factor) == 0):
		found = 1
		if (factor > maxfactor):
			maxfactor = factor
		while ((v % factor) == 0):
			v = v // factor

if (v > maxfactor):
	maxfactor = v
print maxfactor
