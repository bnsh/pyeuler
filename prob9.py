#! /usr/local/bin/python

import math

q = [
	(a*b*math.trunc(math.sqrt(a*a+b*b)))
		for a in xrange(1,1000)
			for b in xrange(a+1,1000) if (
				math.fmod(math.sqrt(a*a+b*b),1) == 0 and
				a+b+math.sqrt(a*a+b*b) == 1000
			)
]
print q[0]
